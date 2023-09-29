from discord.ext import commands
import discord

class Island(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def setup(self, ctx):
        embed1 = discord.Embed(
            title="Welcome to Stage",
            description="Hey there! Welcome to Stage where you set up your island.",
            color=discord.Color.green()
        )
        message = await ctx.send(embed=embed1)

        # Add buttons to the message
        await message.add_reaction('⬅️')
        await message.add_reaction('➡️')
        await message.add_reaction('1️⃣')
        await message.add_reaction('2️⃣')
        await message.add_reaction('3️⃣')
        await message.add_reaction('4️⃣')
        await message.add_reaction('5️⃣')
        await message.add_reaction('✅')
        await message.add_reaction('❌')

        # Define a check function to filter reactions
        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ['⬅️', '➡️', '1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '✅', '❌']

        # Define a variable to keep track of the current page
        current_page = 1

        # Define a list of embeds for the different pages
        embeds = [
            discord.Embed(
                title="Page 1",
                description="This is the first page.",
                color=discord.Color.green()
            ),
            discord.Embed(
                title="Page 2",
                description="This is the second page.",
                color=discord.Color.green()
            ),
            discord.Embed(
                title="Page 3",
                description="This is the third page.",
                color=discord.Color.green()
            )
        ]

        # Define a dictionary of button rows for the different pages
        button_rows = {
            1: ['⬅️', '➡️', '1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '✅', '❌'],
            2: ['⬅️', '➡️', '1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '✅', '❌'],
            3: ['⬅️', '➡️', '1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '✅', '❌']
        }

        # Loop to handle reactions
        while True:
            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
            except:
                break

            if str(reaction.emoji) == '⬅️':
                current_page -= 1
                if current_page < 1:
                    current_page = 1
            elif str(reaction.emoji) == '➡️':
                current_page += 1
                if current_page > len(embeds):
                    current_page = len(embeds)
            elif str(reaction.emoji) == '1️⃣':
                await message.edit(content="You clicked 1️⃣")
            elif str(reaction.emoji) == '2️⃣':
                await message.edit(content="You clicked 2️⃣")
            elif str(reaction.emoji) == '3️⃣':
                await message.edit(content="You clicked 3️⃣")
            elif str(reaction.emoji) == '4️⃣':
                await message.edit(content="You clicked 4️⃣")
            elif str(reaction.emoji) == '5️⃣':
                await message.edit(content="You clicked 5️⃣")
            elif str(reaction.emoji) == '✅':
                await message.edit(content="You clicked ✅")
            elif str(reaction.emoji) == '❌':
                await message.edit(content="You clicked ❌")

            # Update the message with the new embed and button row
            await message.edit(embed=embeds[current_page-1])
            await message.remove_reaction(reaction, user)
            await message.clear_reactions()

            for button in button_rows[current_page]:
                await message.add_reaction(button)

async def setup(bot):
    await bot.add_cog(Island(bot))