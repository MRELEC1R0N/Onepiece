# Function to generate a random location for a server   
# def local_location( setts,local_height1= 225, local_height2 = 425 ):
#     local_breath = 175
#     servers_list = []
#     local_coordinates = []

#     server_coordinates = reserved_collection_name.find_one({"_id": "local_locations"})
#     server_coord_list  = server_coordinates.get("locations", [])
#     server_length = len(server_coord_list)
    




#     for _ in range(setts):
        
#         y_coordinate_1 = random.randint(75, local_height1 if _ % 2 == 0 else local_height2)

#         x_coordinate_1 = random.randint(75, local_breath)

#         y_coordinate_2 = y_coordinate_1
#         y_coordinate_3 = y_coordinate_1 + 50 if y_coordinate_1 <= 125 else y_coordinate_1 - 50
#         y_coordinate_4 = y_coordinate_3 if y_coordinate_1 <= 125 else y_coordinate_3

#         x_coordinate_2 = x_coordinate_1 + 50 if x_coordinate_1 <= 150 else x_coordinate_1 - 50
#         x_coordinate_3 = x_coordinate_1
#         x_coordinate_4 = x_coordinate_2

#         bounds_py = [y_coordinate_1 - 50 if y_coordinate_1 <= 125 else y_coordinate_1 + 50,
#                     y_coordinate_1 - 50 if y_coordinate_1 <= 125 else y_coordinate_1 + 50,
#                     y_coordinate_1 - 50 if y_coordinate_1 <= 125 else y_coordinate_1 + 50,
#                     y_coordinate_3 + 50 if y_coordinate_1 <= 125 else y_coordinate_3 - 50,
#                     y_coordinate_3 + 50 if y_coordinate_1 <= 125 else y_coordinate_3 - 50,
#                     y_coordinate_3 + 50 if y_coordinate_1 <= 125 else y_coordinate_3 - 50,
#                     y_coordinate_1 + 25 if y_coordinate_1 <= 125 else y_coordinate_1 - 25,
#                     y_coordinate_1 + 25 if y_coordinate_1 <= 125 else y_coordinate_1 - 25]

#         bounds_px = [x_coordinate_1 - 50 if x_coordinate_1 <= 150 else x_coordinate_1 + 50,
#                     x_coordinate_1 - 25 if x_coordinate_1 <= 150 else x_coordinate_1 + 25,
#                     x_coordinate_2 + 50,
#                     x_coordinate_1 - 50 if x_coordinate_1 <= 150 else x_coordinate_1 + 50,
#                     x_coordinate_1 - 25 if x_coordinate_1 <= 150 else x_coordinate_1 + 25,
#                     x_coordinate_2 + 50,
#                     x_coordinate_2 + 50,
#                     x_coordinate_1 - 50 if x_coordinate_1 <= 150 else x_coordinate_1 + 50]

#         local_coordinate = {
#             'y_coordinate_1': y_coordinate_1,
#             'x_coordinate_1': x_coordinate_1,
#             'y_coordinate_2': y_coordinate_2,
#             'x_coordinate_2': x_coordinate_2,
#             'y_coordinate_3': y_coordinate_3,
#             'x_coordinate_3': x_coordinate_3,
#             'y_coordinate_4': y_coordinate_4,
#             'x_coordinate_4': x_coordinate_4
#         }
#         server_boundries = {}
#         for i in range(8):
#             server_boundries['bound_px_' + str(i+1)] = bounds_px[i]
#             server_boundries['bound_py_' + str(i+1)] = bounds_py[i]
#         local_coordinate['server_boundries'] = server_boundries

#         local_coordinates.append(local_coordinate)

#     server_numbers = []
#     for i, local_coordinate in enumerate(local_coordinates):
#         server_numbers.append(f"server_{server_length + i}")
#         server_numbers[i] = {}
#         for key, value in local_coordinate.items():
#             server_numbers[i].update({key: value})

#         servers_list.append({f"server_coordiante": server_numbers[i]})

#     reserved_collection_name.update_one({"_id": "local_locations"}, {"$push": {"locations": {"$each": servers_list}}})

#     print('succes')




# Import discord and commands modules
# import discord
# from discord.ext import commands

# # Create a bot instance
# bot = commands.Bot(command_prefix="!")

# # Define a command called island
# @bot.command()
# async def island(ctx):
#     # Create an embed object
#     embed = discord.Embed(
#         title="Create your own island",
#         description="Please fill in the following details to create your own island for the game",
#         color=discord.Color.green()
#     )

#     # Add fields to the embed object
#     embed.add_field(name="Name", value="Enter the name of your island", inline=False)
#     embed.add_field(name="Type", value="Choose from desert, forest, snow, mountain, sky, underwater, etc.", inline=False)
#     embed.add_field(name="Size", value="Choose a number from 1 to 10, where 1 is the smallest and 10 is the largest", inline=False)
#     embed.add_field(name="Layout", value="Describe how you want to arrange the areas and landmarks on your island, such as ports, markets, towns, villages, temples, ruins, caves, etc.", inline=False)
#     embed.add_field(name="Theme", value="Choose what kind of atmosphere and style you want your island to have, such as pirate, marine, ancient, modern, fantasy, etc.", inline=False)
#     embed.add_field(name="Inhabitants", value="Describe what kind of people and creatures live on your island, such as humans, animals, monsters, etc.", inline=False)
#     embed.add_field(name="Events", value="Describe what kind of events and quests happen on your island, such as battles, puzzles, mysteries, festivals, etc.", inline=False)

#     # Send the embed message to the channel
#     await ctx.send(embed=embed)




# I understand, you want to make the temple, ruins, and cave more random and mysterious for your game. That's a good idea, as it will add more surprise and challenge to your game. Here is a possible list of basic things that you can ask your users to choose from when creating their island layout, without the temple, ruins, and cave:

# - Port: A port is a place where ships can dock and trade goods. You can ask your users if they want a port on their island, and if yes, how big and on what location of the island they want it. For example, you can use a scale of 1 to 5, where 1 is the smallest and 5 is the largest, and you can use directions such as north, south, east, west, northeast, northwest, southeast, southwest, center, etc.
# - Market: A market is a place where people can buy and sell various items and services. You can ask your users if they want a market on their island, and if yes, how big and on what location of the island they want it. For example, you can use the same scale and directions as for the port.
# - Town: A town is a place where people live and work. You can ask your users if they want a town on their island, and if yes, how big and on what location of the island they want it. For example, you can use the same scale and directions as for the port and the market.
# - Village: A village is a smaller place than a town where people live and work. You can ask your users if they want a village on their island, and if yes, how big and on what location of the island they want it. For example, you can use the same scale and directions as for the other places.
# - Farm: A farm is a place where crops are grown and animals are raised. You can ask your users if they want a farm on their island, and if yes, how big and on what location of the island they want it. For example, you can use the same scale and directions as for the other places.
# - Fort: A fort is a place where soldiers or pirates defend themselves from enemies. You can ask your users if they want a fort on their island, and if yes, how big and on what location of the island they want it. For example, you can use the same scale and directions as for the other places.
# - Lighthouse: A lighthouse is a tower that emits light to guide ships at sea. You can ask your users if they want a lighthouse on their island, and if yes, how big and on what location of the island they want it. For example, you can use the same scale and directions as for the other places.

# These are some basic things that you can ask your users to choose from when creating their island layout, without the temple, ruins, and cave. Of course, you can also add more options and features to make your island layout more diverse and interesting. I hope this helps you with your game development. Have fun! 😊




#test this funtion for 
# generated_coordinates = []
# def local_location(setts, local_height=10000, local_breath=10000):
#     global generated_coordinates

#     # Create a buffer around the previously generated coordinates
#     if generated_coordinates:
#         buffer_distance = 150  #will be giving it a range in future 
#         buffer_polygons = [Point(coord).buffer(buffer_distance) for coord in generated_coordinates]
#         buffer_union = cascaded_union(buffer_polygons)
#     else:
#         buffer_union = None

#     # Generate coordinates until unique coordinates are found
#     while True:
#         x_coordinate = random.randint(0, local_breath)
#         y_coordinate = random.randint(0, local_height)
#         new_coordinate = (x_coordinate, y_coordinate)
        
#         # Check if coordinates already exist in the buffer
#         if buffer_union is None or not buffer_union.contains(Point(new_coordinate)):
#             break

#     # Add the new coordinates to the list
#     generated_coordinates.append(new_coordinate)
    
#     # Store the new coordinates in the MongoDB collection
#     try:
#         reserved_collection_name.update_one({"_id": "local_locations"}, {"$push": {"locations": {"$each":new_coordinate}}})
#     except Exception as e:
#         print(f"Error storing coordinates in MongoDB: {str(e)}")







'''With this code i made a bigger map by adding the current maps'''

# # Import the Image class from the Pillow library
# from PIL import Image

# # Open the images you want to merge and store them in a list
# images = [Image.open("E:\one_piece_bot\IMAGES\clear.jpg"), Image.open("E:\\one_piece_bot\\IMAGES\\clear - Copy.jpg"), Image.open("E:\\one_piece_bot\\IMAGES\\clear - Copy (2).jpg"), Image.open("E:\\one_piece_bot\\IMAGES\\clear - Copy (3).jpg")]

# # Calculate the total width and maximum height of the final image
# total_width = 0
# max_height = 0
# for image in images:
#     width, height = image.size
#     total_width += width
#     if height > max_height:
#         max_height = height

# # Create a new image with the appropriate mode, width and height
# new_image = Image.new("RGB", (total_width, max_height))

# # Paste the images one by one to the new image and update the x-offset
# x_offset = 0
# for image in images:
#     new_image.paste(image, (x_offset, 0))
#     x_offset += image.size[0]

# # Save the new image
# new_image.save("E:\\one_piece_bot\\IMAGES\\clear_extra.jpg")