import discord
from discord.ext import commands
from map import  map_matrix,generate_coordinates , design_map 
from database import collection_name  ,reserved_collection_name as rc
from extra_function import add_parts_to_island as island




class start(commands.Cog):
    @commands.command()
    async def Start(self, ctx):
        await ctx.send('I am working fine')


    
    @commands.command()
    async def mapdata(self,ctx):
        island(server_id=ctx.guild.id)
        await ctx.send('Inserted successfully')        
    

    @commands.command()
    async def map_image(self,ctx):
        design_map(server_id=ctx.guild.id,server_name=ctx.guild.name)
        await ctx.send("Image has been generated")






    @commands.command()
    async def delete(self,ctx): 
        collection_name.delete_one({'_id':ctx.guild.id})



    @commands.command()
    async def test(self, ctx):
        ''' In this at moment we are trying to import  the server details and store it in mongo db collection '''
        coordinatess = rc.find_one({"_id": "local_locations"})
        coordinates = coordinatess['locations'][-1]
    
        # Construct the server_info dictionary
        server_info = {
            "_id": ctx.guild.id,
            "guild_id": ctx.guild.id,
            "guild_name": ctx.guild.name,
            "guild_pfp": str(ctx.guild.icon.url) if ctx.guild.icon else None,
            "owner_id": ctx.guild.owner_id,
            "Coordinates":coordinates
            # Add other fields if needed
        }


        # # Update or insert server information in the database
        collection_name.insert_one(server_info)
        collection_name.update_one({"_id": "local_locations"}, {"$pop": {"locations": -1}})
        
        
        await ctx.send('Inserted successfully')







    @commands.command()
    async def mapt(self , ctx):
        map_matrix()
        await ctx.send('Inserted successfully')

        

    @commands.command()
    async def generate_coordinates(self,ctx,num_points):
        generate_coordinates(int(num_points))
        await ctx.send(f"{num_points} local location added")


async def setup(bot):
    await bot.add_cog(start(bot))