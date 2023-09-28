import tracemalloc
import discord 
from discord.ext import commands
import Settings
from database import reserved_collection_name as rc , collection_name

# Set up the logger
logger = Settings.logging.getLogger("bot")
2
# Define the function to run the bot
def run():
    intents = discord.Intents.all()
    # intents.message_content = True

    bot = commands.Bot(command_prefix="!", intents=intents)

    # Load all cogs on bot ready
    async def load_cogs():
        for cog_file in Settings.CMDS_DIR.glob("*.py"):
            if cog_file.is_file():
                await bot.load_extension(f"Cmds.{cog_file.stem}")
                logger.info(f"Loaded {cog_file.stem}")

    @bot.event
    async def on_ready():
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")
        await load_cogs()

    for cmd in ['load', 'unload', 'reload']:
        @bot.command(name=  cmd)
        async def _cmd(ctx, cog: str):
            try:
                await getattr(bot, f'{cmd}_extension')(f"Cmds.{cog.lower()}")
                await ctx.send(f'Done {cmd}ing')
            except Exception as e:
                await ctx.send(f'Error: {e}')
    @bot.event
    async def on_guild_join(guild):
        coordinatess = rc.find_one({"_id": "local_locations"})
        coordinates = coordinatess['locations'][0]

        # Construct the server_info dictionary
        server_info = {
            "_id": guild.id,
            "guild_id": guild.id,
            "guild_name": guild.name,
            "guild_pfp": str(guild.icon.url) if guild.icon else None,
            "owner_id": guild.owner_id,
            "Coordinates":coordinates
            # Add other fields if needed
        }
    
        collection_name.insert_one(server_info)
        rc.update_one({"_id": "local_locations"}, {"$pop": {"locations": -1}})   

    # Start bot with tracemalloc for memory tracking
    tracemalloc.start()
    bot.run(Settings.Discord_api, root_logger=True)

if __name__ == "__main__":
    run()
