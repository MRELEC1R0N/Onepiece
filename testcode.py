# from pymongo import MongoClient

# client = MongoClient('mongodb+srv://thecgman60:iamragnarok04123@cluster0.yy14chf.mongodb.net/')
# database_name = client['Onepiece']
# collection_name = database_name['Server_info']

# server_data = collection_name.find_one({'_id': 1120040588339843200})
# print(server_data)

# from pymongo import MongoClient

# client = MongoClient('mongodb+srv://thecgman60:iamragnarok04123@cluster0.yy14chf.mongodb.net/')
# db = client["Onepiece"]
# collection = db["Server_info"]

# data = collection.find_one({"_id":1120040588339843172})

# if data is not None:
#     data1 = data["guild_name"]
#     print(data1)
# else:
#     print("No document found with the specified ID.")



# from PIL import Image

# def check_image(image_path):
#     try:
#         image = Image.open(image_path)
#         image.show()
#         print("Image loaded successfully.")
#     except Exception as e:
#         print(f"Error loading the image: {e}")

# image3_path = 'E:\\Onepiecebot\\IMAGES\\darkb.jpg'
# check_image(image3_path)




# import cv2

# def check_image(image_path):
#     try:
#         image = cv2.imread(image_path)
#         cv2.imshow("Image", image)
#         cv2.waitKey(0)
#         cv2.destroyAllWindows()
#         print("Image loaded successfully.")
#     except Exception as e:
#         print(f"Error loading the image: {e}")

# image3_path = 'E:\\Onepiecebot\\IMAGES\\dblue.png'
# check_image(image3_path)
# import discord
# from discord.ext import commands



# intents = discord.Intents.all()
# intents.members = True
# intents.reactions = True

# bot = commands.Bot(command_prefix='!' , intents= intents)

# @bot.event
# async def on_ready():
#     print(f'{bot.user.name} has connected to Discord!')

# @bot.command(name='start')
# async def start(ctx):
#     guild = ctx.guild

#     # Check if there is a channel with name Bot_logs
#     bot_logs_channel = discord.utils.get(guild.channels, name='Bot_logs')
#     if bot_logs_channel is None:
#         # If no, create one
#         overwrites = {
#             guild.default_role: discord.PermissionOverwrite(read_messages=False),
#             guild.me: discord.PermissionOverwrite(read_messages=True)
#         }
#         bot_logs_channel = await guild.create_text_channel('Bot_logs', overwrites=overwrites)

#     # Check if there is a role named Team
#     team_role = discord.utils.get(guild.roles, name='Team')
#     if team_role is None:
#         # If no, create one
#         team_role = await guild.create_role(name='Team')

#     @bot.command(name='setup')
#     async def setup(ctx):
#         guild = ctx.guild

#         # Check if there is a channel with name verification
#         verification_channel = discord.utils.get(guild.channels, name='verification')
#         if verification_channel is None:
#             # If no, create one
#             overwrites = {
#                 guild.default_role: discord.PermissionOverwrite(read_messages=True),
#                 guild.me: discord.PermissionOverwrite(read_messages=True)
#             }
#             verification_channel = await guild.create_text_channel('verification', overwrites=overwrites)

#             # Send an embed with 2 roles info
#             embed = discord.Embed(title="Roles Info", description="React with the corresponding emoji to get the role", color=0x00ff00)
#             embed.add_field(name="Team", value="React with 👥", inline=False)
#             embed.add_field(name="Client", value="React with 🧑‍💼", inline=False)
#             message = await verification_channel.send(embed=embed)

#             # Add reactions to the message
#             await message.add_reaction('👥')
#             await message.add_reaction('🧑‍💼')

#             @bot.event
#             async def on_raw_reaction_add(payload):
#                 if payload.message_id == message.id:
#                     guild = bot.get_guild(payload.guild_id)
#                     member = guild.get_member(payload.user_id)

#                     if str(payload.emoji) == '👥':
#                         # Pass a message in bot_log chat : No role was assigned as it is still under test
#                         await bot_logs_channel.send(f"No role was assigned as it is still under test by {member.mention}")
#                     elif str(payload.emoji) == '🧑‍💼':
#                         # Create a role with user id of the user and assign it to that user and make a channel with the username and id in brackets
#                         role_name = f"{member.name} ({member.id})"
#                         member_role = await guild.create_role(name=role_name)
#                         await member.add_roles(member_role)

#                         channel_name = f"{member.name} ({member.id})"
#                         overwrites = {
#                             guild.default_role: discord.PermissionOverwrite(read_messages=False),
#                             member_role: discord.PermissionOverwrite(read_messages=True),
#                             member: discord.PermissionOverwrite(read_messages=True)
#                         }
#                         member_channel = await guild.create_text_channel(channel_name, overwrites=overwrites)

#                         # Make sure only people who have team role and user who's id is in the channel name have access to that channel 
#                         @bot.event
#                         async def on_voice_state_update(member, before, after):
#                             if after.channel == member_channel:
#                                 team_role = discord.utils.get(guild.roles, name='Team')
#                                 if team_role not in member.roles and str(member.id) not in member_channel.name:
#                                     await member.move_to(None)

#                                 for channel in guild.voice_channels:
#                                     if str(member.id) in channel.name and channel != member_channel:
#                                         await member.move_to(None)

#                                 for channel in guild.text_channels:
#                                     if str(member.id) in channel.name and channel != member_channel:
#                                         await channel.set_permissions(team_role, read_messages=True)
#                                     else:
#                                         await channel.set_permissions(team_role, read_messages=False)

#         else:
#             await ctx.send("Verification channel already exists")



# bot.run('MTExODE2NzY4ODM1MTU5MjUxOA.Gz3roQ.sInLO4aC_WUzi4F1KNC2PmJeRB4jrOM1BSsTa4')



# import discord
# from discord.ext import commands


# intents = discord.Intents.all()
# bot = commands.Bot(command_prefix='!' , intents=intents)

# @bot.command()
# async def setup(self , ctx):
#     await ctx.send('i am alive')
#     guild = ctx.guild
#     verification_channel = discord.utils.get(guild.channels, name='verification')
#     if not verification_channel:
#         overwrites = {
#             guild.default_role: discord.PermissionOverwrite(send_messages=False),
#             guild.owner: discord.PermissionOverwrite(send_messages=True),
#             bot.user: discord.PermissionOverwrite(send_messages=True)
#         }
#         verification_channel = await guild.create_text_channel('verification', overwrites=overwrites)
#     embed = discord.Embed(title="Verification", description="React to this message to get verified.")
#     embed.add_field(name="Client", value="React with 👤 to get the Client role and a private channel.")
#     embed.add_field(name="Form", value="React with 📝 to get a form sent to you via DM.")
#     message = await verification_channel.send(embed=embed)
#     await message.add_reaction("👤")
#     await message.add_reaction("📝")

# @bot.event
# async def on_raw_reaction_add(payload):
#     if payload.member == bot.user:
#         return
#     guild = bot.get_guild(payload.guild_id)
#     channel = bot.get_channel(payload.channel_id)
#     message = await channel.fetch_message(payload.message_id)
#     if message.author != bot.user:
#         return
#     if payload.emoji.name == "👤":
#         role_name = f"Client-{payload.member.id}"
#         role = discord.utils.get(guild.roles, name=role_name)
#         if not role:
#             role = await guild.create_role(name=role_name)
#             overwrites = {
#                 guild.default_role: discord.PermissionOverwrite(read_messages=False),
#                 guild.owner: discord.PermissionOverwrite(read_messages=True),
#                 bot.user: discord.PermissionOverwrite(read_messages=True),
#                 role: discord.PermissionOverwrite(read_messages=True)
#             }
#             channel_name = f"{payload.member.name}-{payload.member.discriminator}"
#             await guild.create_text_channel(channel_name, overwrites=overwrites)
#         await payload.member.add_roles(role)
#     elif payload.emoji.name == "📝":
#         embed = discord.Embed(title="Form", description="Please fill out this form and send it back via DM.")
#         embed.add_field(name="Name", value="Your full name")
#         embed.add_field(name="Email", value="Your email address")
#         embed.add_field(name="Address", value="Your mailing address")
#         await payload.member.send(embed=embed)

# @bot.event
# async def on_raw_reaction_remove(payload):
#     guild = bot.get_guild(payload.guild_id)
#     channel = bot.get_channel(payload.channel_id)
#     message = await channel.fetch_message(payload.message_id)
#     if message.author != bot.user:
#         return
#     member = guild.get_member(payload.user_id)
#     if payload.emoji.name == "👤":
#         role_name = f"Client-{member.id}"
#         role = discord.utils.get(guild.roles, name=role_name)
#         if role:
#             await member.remove_roles(role)
#             await role.delete()
#             channel_name = f"{member.name}-{member.discriminator}"
#             private_channel = discord.utils.get(guild.channels, name=channel_name)
#             if private_channel:
#                 await private_channel.delete()

# @bot.event
# async def on_message(message):
#     if message.author == bot.user or not isinstance(message.channel, discord.DMChannel):
#         return
#     form_channel = discord.utils.get(message.guild.channels, name='form')
#     if not form_channel:
#         overwrites = {
#             message.guild.default_role: discord.PermissionOverwrite(send_messages=False),
#             message.guild.owner: discord.PermissionOverwrite(send_messages=True),
#             bot.user: discord.PermissionOverwrite(send_messages=True)
#         }
#         form_channel = await message.guild.create_text_channel('form', overwrites=overwrites)
#     embed = discord.Embed(title=f"Form from {message.author}", description=message.content)
#     await form_channel.send(embed=embed)

# bot.run('MTAwOTQ3NzAyMzg4ODA2NDYxMw.G9nFug.XmiPynlradAQhZD9_ZYT-4BnL_n3tN-chodiEg')














# from database import collection_name


# data = collection_name.find_one({"_id":1120040588339843172})
# for i in range(8):
#                 data1 = data["Nearest_local"][i][f'local_square_{i}'][0]['X_coordinate']
#                 data2 = data["Nearest_local"][i][f'local_square_{i}'][1]['Y_coordinate']
#                 print(data1, data2)














# import random





# mapWidth = 10000
# mapHeight = 10000
# local_width = 150
# local_height = 400


# for i in range(1):
#     coord = {}
#     for i in range(1):
#         # Generate random X and Y coordinates
#         global serverX1
#         serverX1 = random.randint(0, mapWidth - 1)
#         global serverY1
#         serverY1 = random.randint(0, mapHeight - 1)

#         # this lines need an update that decidieds rather the coordinate will go up or down
#         global serverX2
#         serverX2 = (serverX1 - 1)
#         global serverY2
#         serverY2 = (serverY1 - 1)
        
#         coord.update({'X_coordinate_1':serverX1})
#         coord.update({'Y_coordinate_1':serverY1})
        
#         coord.update({'X_coordinate_2':serverX2})
#         coord.update({'Y_coordinate_2':serverY2})

#         global lmapX1
#         lmapX1 = random.randint(50,local_width -1)
#         global lmapY1
#         lmapY1 = random.randint(50 ,local_height - 1)

#         # this lines need an update that decidieds rather the coordinate will go up or down
#         global lmapX2
#         global lmapX3
#         global lmapX4
#         if lmapX1 >=  75:
#             lmapX2 = (lmapX1 -1)
#             lmapX3 = (lmapX2)
#             lmapX4 = (lmapX1)

#         else :
#             lmapX2 = (lmapX1 + 1)
#             lmapX3 = (lmapX2)
#             lmapX4 = (lmapX1)

#         global lmapY2
#         global lmapY3
#         global lmapY4
#         if lmapY1 >=  200:
#             lmapY2 = (lmapY1 -1)
#             lmapY3 = (lmapY1)
#             lmapY4 = (lmapY2)

#         else :
#             lmapY2 = (lmapY1 +1)
#             lmapY3 = (lmapY1)
#             lmapY4 = (lmapY2)
                
#         coord.update({'X_local_1':lmapX1})
#         coord.update({'Y_local_1':lmapY1})
        
#         coord.update({'X_local_2':lmapX2})
#         coord.update({'Y_local_2':lmapY2})  

#         coord.update({'X_local_3':lmapX3})
#         coord.update({'Y_local_3':lmapY3})

#         coord.update({'X_local_4':lmapX4})
#         coord.update({'Y_local_4':lmapY4})

#         nearest_coordinates = []
#         for dx in range(-2, 3):
#             for dy in range(-2, 3):
                
#                 if dx == 0 and dy == 0:
#                     continue

#                 nearestX = serverX1 + dx
#                 nearestY = serverY1 + dy

#                 nearest_coordinates.append((nearestX, nearestY))
                
#         local_coordinates = []
#         for dx in range(-2, 3):
#             for dy in range(-2, 3):
#                 # Exclude the center coordinate itself
#                 if dx == 0 and dy == 0:
#                     continue

#                 local_mapX = lmapX1 + dx
#                 local_mapY = lmapY1 + dy

#                 local_coordinates.append((local_mapX, local_mapY))

#         ex_val = 0
#         for coordinates in nearest_coordinates:
#             coord.update({f'square_{ex_val}':[{'X_coordinate':coordinates[0]} ,{'Y_coordinate':coordinates[1]} ]})
#             ex_val = ex_val + 1

#         l_val = 0
#         for coordinates in local_coordinates:
#             coord.update({f'local_square_{l_val}':[{'X_coordinate':coordinates[0]} ,{'Y_coordinate':coordinates[1]} ]})
#             l_val = l_val + 1

#     for i in coord:
#         print(coord[i])

# from PIL import Image
# from database import collection_name
# import requests
# from io import BytesIO


# for i in range(1):
#     # In this function, we are going to decorate our map with territories and server ids
#     # coord = {}
#             server_id = collection_name.find_one({'_id': 1120040588339843172})
    
#             if server_id is not None:
#                 server_pfp_url = server_id['guild_pfp']
#     #     X_1 , Y_1 ,X_2 , Y_2 , X_3 , Y_3 , X_4 , Y_4 = server_id['local_cod']['X_cod_1'], server_id['local_cod']['Y_cod_1'] , server_id['local_cod']['X_cod_2'], server_id['local_cod']['Y_cod_2']  , server_id['local_cod']['X_cod_3'], server_id['local_cod']['Y_cod_3'] ,server_id['local_cod']['X_cod_4'], server_id['local_cod']['Y_cod_4']

#         # x_cod, y_cod = server_id['X_map'], server_id['Y_map']

#             image1_path='E:\\ONEPIECEBOT\\IMAGES\\clear.jpg'
#             image2_url=server_pfp_url
#             # Open the first image
#             image1 = Image.open(image1_path)

#             # Download the second image from the URL
#             response = requests.get(image2_url)
#             image2 = Image.open(BytesIO(response.content))


#             image2 = image2.resize(image1.size)
#             # Convert image2 to match the mode of image1
#             image2 = image2.convert(image1.mode)

#             # Check if the sizes of the two images are the same
#             if image1.size == image2.size:
#                 print("The sizes of the two images are the same")
#             else:
#                 print("The sizes of the two images are different")

#             # Check if the modes of the two images are the same
#             if image1.mode == image2.mode:
#                 print("The modes of the two images are the same")
#             else:
#                 print("The modes of the two images are different")






# from PIL import Image

# def resize_to_embed_size(merged_image_path = 'E:\\ONEPIECEBOT\\IMAGES\\merged_image.png'):
#     # Open the merged image
#     merged_image = Image.open(merged_image_path)

#     # Print the original image size
#     print(f"Original Image Size: {merged_image.width}x{merged_image.height}")

#     # Define the maximum dimensions for an embed thumbnail
#     max_width = 1024
#     max_height = 1024

#     # Check if the merged image needs to be resized
#     if merged_image.width > max_width or merged_image.height > max_height:
#         # Calculate the aspect ratio to maintain the original image's proportions
#         aspect_ratio = merged_image.width / merged_image.height

#         # Calculate the new dimensions to fit within the embed size
#         if aspect_ratio >= 1:
#             new_width = max_width
#             new_height = int(max_width / aspect_ratio)
#         else:
#             new_height = max_height
#             new_width = int(max_height * aspect_ratio)

#         # Resize the image
#         resized_image = merged_image.resize((new_width, new_height))

#         # Print the resized image size
#         print(f"Resized Image Size: {resized_image.width}x{resized_image.height}")
#         return resized_image
#     else:
#         # If the image doesn't need resizing, print the original image size
#         print(f"No Resizing Required. Image Size: {merged_image.width}x{merged_image.height}")
#         return merged_image

# resize_to_embed_size()
# from PIL import Image

# def resize_image(image_path = 'E:\\ONEPIECEBOT\\IMAGES\\merged_image.png', max_size = 1024):
#     # Open the image
#     image = Image.open(image_path)

#     # Get the original size
#     width, height = image.size

#     # Check if the image needs resizing
#     if width > max_size or height > max_size:
#         # Calculate the new size while maintaining the aspect ratio
#         if width > height:
#             new_width = max_size
#             new_height = int(height * max_size / width)
#         else:
#             new_height = max_size
#             new_width = int(width * max_size / height)

#         # Resize the image
#         image = image.resize((new_width, new_height))

#     # Save the resized image to a new file (optional)
#     resized_image_path = "resized_image.png"
#     image.save(resized_image_path)

#     return resized_image_path

# # Usage example




# resize_image()


# from PIL import Image

# def resize_and_rotate_image(image_path, max_size):
#     # Open the image
#     image = Image.open(image_path)

#     # Get the original size
#     width, height = image.size

#     # Rotate the image 90 degrees (change length to breadth and breadth to length)
#     rotated_image = image.transpose(Image.Transpose.ROTATE_90)

#     # Check if the rotated image needs resizing
#     if width > max_size or height > max_size:
#         # Calculate the new size while maintaining the aspect ratio
#         if height > width:
#             new_width = max_size
#             new_height = int(width * max_size / height)
#         else:
#             new_height = max_size
#             new_width = int(height * max_size / width)

#         # Resize the rotated image
#         resized_rotated_image = rotated_image.resize((new_width, new_height))

#     else:
#         # No resizing needed if the image is within the max size limits
#         resized_rotated_image = rotated_image

#     # Save the resized and rotated image to a new file (optional)
#     resized_rotated_image_path = "resized_rotated_image.png"
#     resized_rotated_image.save(resized_rotated_image_path)

#     return resized_rotated_image_path

# # Usage example
# original_image_path = "E:\\ONEPIECEBOT\\IMAGES\\merged_image.png"
# max_embed_size = 2048
# resized_rotated_image_path = resize_and_rotate_image(original_image_path, max_embed_size)










# from database import reserved_collection_name





# # Assuming you have already connected to the MongoDB database and have the appropriate collection object
# reserved_collection_name.insert_one({"_id": "mapstatus", "mapstatus": 0})









# import random

# def mass_local_locations():
#     height_1 = 200
#     breath = 200
#     height_2 = 400
    
#     coord = {}
#     y_1 = random.randint(50, breath)
#     local_servers = []
#     a = 0
        
#     for _ in range(500):


#         lmapY1 = random.randint(50 ,height_1 - 1)
#         lmapX1 = lmapY1

#         if lmapX1 >=  75:
#             lmapX2 = (lmapX1 -1)
#             lmapX3 = (lmapX2)
#             lmapX4 = (lmapX1)

#         else :
#             lmapX2 = (lmapX1 + 1)
#             lmapX3 = (lmapX2)
#             lmapX4 = (lmapX1)

#         if lmapY1 >=  200:
#             lmapY2 = (lmapY1 -1)
#             lmapY3 = (lmapY1)
#             lmapY4 = (lmapY2)

#         else :
#             lmapY2 = (lmapY1 +1)
#             lmapY3 = (lmapY1)
#             lmapY4 = (lmapY2)
                                
#         coord.update({'X_local_1':lmapX1})
#         coord.update({'Y_local_1':lmapY1})
                        
#         coord.update({'X_local_2':lmapX2})
#         coord.update({'Y_local_2':lmapY2})  

#         coord.update({'X_local_3':lmapX3})
#         coord.update({'Y_local_3':lmapY3})

#         coord.update({'X_local_4':lmapX4})
#         coord.update({'Y_local_4':lmapY4})


#         local_coordinates = []
#         for dx in range(-1, 2):
#             for dy in range(-1, 2):
#                                 # Exclude the center coordinate itself
#                 if dx == 0 and dy == 0:
#                                     continue

#                 local_mapX = lmapX1 + dx * 50  # Add 50 units to X
#                 local_mapY = lmapY1 + dy * 50  # Add 50 units to Y

#                 local_coordinates.append({'X_coordinate': local_mapX, 'Y_coordinate': local_mapY})

#         l_val = 0
#         for coordinates in local_coordinates :
#             coord.update({f'local_square_{l_val}':coordinates})
#             l_val = l_val + 1

        
#         for key , value in coord.items():
#             print( key , value)
#         print(a)
#         a = a + 1
    

    #         # Generating local coordinates for upper servers
    #         x_1 = random.randint(50, height_1)
    #         local_server = {"x_coordinate": x_1, "y_coordinate": y_1}
    #         local_servers.append(local_server)
    #         coord.append({"local_server": local_server})
    #         for dx in range(-1 , 2 ):
    #             for dy in range (-1, 2):
    #                 if dx == 0 and dy == 0:
    #                     continue

    #                 local_mapX = x_1 + dx * 50  # Add 50 units to X
    #                 local_mapY = y_1 + dy * 50  # Add 50 units to Y

    #                 local_coordinates = {'X_coordinate': local_mapX, 'Y_coordinate': local_mapY}
    #                 coord.append({"local_coordinates": local_coordinates})

    # for c in coord:
    #      print(c)
         
# mass_local_locations()


# mass_local_locations()





            


        # '''Generating local cordinates '''
        # x_1 = random.randint(50, height_2)
        # loca_cordinates = []

        # for dx in range(-1 , 2 ):
        #      for dy in range (-1,2):
        #          if dx == 0 and dy == 0:
        #              continue
        #          loca_cordinates.append({'X_coordinate': x_1 + dx, 'Y_coordinate': y_1 + dy})












# def local_cordinates():
#     length_1 = 275
#     length_2 = 425
#     breath = 175
    
#     coord = {}
#     for i in range(1):
        # lmapx1 = random.randint(75 ,breath)
        # lmapy1 = random.randint(75 ,length_1)

        # lmapx2 = lmapx1
        # lmapy2 = lmapy1+50

        # lmapx3 = lmapx1+50
        # lmapy3 = lmapy1

        # lmapx4 = lmapx1+50
        # lmapy4 = lmapy1+50

    #     firstpoint = {'coordinates':[{'X_local_1':lmapx1},{'Y_local_1':lmapy1}]}

    #     coord.update(firstpoint)

    # for key, value in coord.items():
    #     print(f"{key} has location {value}")

# def local_coordinates():
#     length_1 = 275
#     length_2 = 425
#     breath = 175

#     coord = {}
#     for i in range(1):
#         lmapx1 = random.randint(75, breath)
#         lmapy1 = random.randint(75, length_1)

#         boxes = []
#         for j in range(9):
#             lmapx = lmapx1 + (j % 3 - 1) * 50
#             lmapy = lmapy1 + ((j // 3 - 1) * -1) * 50

#             box = {'X_coordinate': lmapx, 'Y_coordinate': lmapy}
#             boxes.append(box)

#         coord['local_boxes'] = boxes

#         firstpoint = {'coordinates': [{'X_local_1': lmapx1}, {'Y_local_1': lmapy1}]}
#         coord.update(firstpoint)

#     for key, value in coord.items():
#         if key == 'local_boxes':
#             print(f"{key} has locations:")
#             for i, box in enumerate(value):
#                 print(f"Box {i+1}: X_coordinate={box['X_coordinate']}, Y_coordinate={box['Y_coordinate']}")
#         else:
#             print(f"{key} has location {value}")


# def local_coordinates():
#     length_1 = 275
#     length_2 = 425
#     breath = 175

#     coord = {}
#     for i in range(1):
#         lmapx1 = random.randint(75, breath)
#         lmapy1 = random.randint(75, length_1)

#         lmapx2 = lmapx1
#         lmapy2 = lmapy1 + 50

#         lmapx3 = lmapx1 + 50
#         lmapy3 = lmapy1

#         lmapx4 = lmapx1 + 50
#         lmapy4 = lmapy1 + 50

#         boxes = []
#         for j, (x, y) in enumerate([(lmapx1, lmapy1), (lmapx2, lmapy2), (lmapx3, lmapy3), (lmapx4, lmapy4)]):
#             box = {'X_coordinate': x, 'Y_coordinate': y}
#             boxes.append(box)

#         coord['local_boxes'] = boxes

#         firstpoint = {'coordinates': [{'X_local_1': lmapx1}, {'Y_local_1': lmapy1}]}
#         coord.update(firstpoint)

#         remaining_points = {
#             'lmap2': {'X': lmapx2, 'Y': lmapy2},
#             'lmap3': {'X': lmapx3, 'Y': lmapy3},
#             'lmap4': {'X': lmapx4, 'Y': lmapy4}
#         }
#         coord.update(remaining_points)

#         local_coordinates = []
#         for dx in range(-1, 2):
#             for dy in range(-1, 2):
#             # Exclude the center coordinate itself
#                 if dx == 0 and dy == 0:
#                     continue

#                 local_mapX = lmapx1 + dx * 50  # Add 50 units to X
#                 local_mapY = lmapy1 + dy * 50  # Add 50 units to Y

#                 local_coordinates.append({'X_coordinate': local_mapX, 'Y_coordinate': local_mapY})

#                 l_val = 0
#                 for coordinates in local_coordinates:
#                     coord.update({f'local_square_{l_val}':coordinates})
#                     l_val = l_val + 1



    # for key, value in coord.items():
    #     if key == 'local_boxes':
    #         print(f"{key} has locations:")
    #         for i, box in enumerate(value):
    #             print(f"Box {i+1}: X_coordinate={box['X_coordinate']}, Y_coordinate={box['Y_coordinate']}")
    #     else:
    #         print(f"{key} has location {value}")





# import random


# def local_coordinates():
#     length_1 = 275
#     length_2 = 425
#     breath = 175

#     coord = {}
#     # Remove the for loop and just generate one set of local_boxes and new_boxes
#     lmapx1 = random.randint(75, breath)
#     lmapy1 = random.randint(75, length_1)

#     lmapx2 = lmapx1
#     lmapy2 = lmapy1 + 50

#     lmapx3 = lmapx1 + 50
#     lmapy3 = lmapy1

#     lmapx4 = lmapx1 + 50
#     lmapy4 = lmapy1 + 50

#     boxes = [
#         {'X_coordinate': lmapx1, 'Y_coordinate': lmapy1},
#         {'X_coordinate': lmapx2, 'Y_coordinate': lmapy2},
#         {'X_coordinate': lmapx3, 'Y_coordinate': lmapy3},
#         {'X_coordinate': lmapx4, 'Y_coordinate': lmapy4}
#     ]
#     coord['local_boxes'] = boxes

    # To generate points of a square that is overlapping on this square and is double in size, you can use the following formula:
    # x' = x + (w/2) * (cos(theta) - 1) - (h/2) * sin(theta)
    # y' = y + (h/2) * (cos(theta) - 1) + (w/2) * sin(theta)
    # where x and y are the original coordinates, w and h are the width and height of the original square, theta is the angle of rotation, and x' and y' are the new coordinates.

    # Assuming that the original square is not rotated, theta is zero and the formula simplifies to:
    # x' = x - w/4
    # y' = y - h/4

#     w = 50 # The width of the original square
#     h = 50 # The height of the original square

#     # To generate the new points, we can loop through the original points and apply the formula:
#     new_boxes = []
#     for box in boxes:
#         x = box['X_coordinate']
#         y = box['Y_coordinate']
#         x_prime = x - w/4
#         y_prime = y - h/4
#         new_box = {'X_coordinate': x_prime, 'Y_coordinate': y_prime}
#         new_boxes.append(new_box)

#     coord['new_boxes'] = new_boxes

#     # To print the points of the local_boxes and the new_boxes, you can use a for loop like this:
#     for i in range(len(coord['local_boxes'])):
#         local_box = coord['local_boxes'][i]
#         new_box = coord['new_boxes'][i]
#         print(f"Local box {i+1}: ({local_box['X_coordinate']}, {local_box['Y_coordinate']})")
#         print(f"New box {i+1}: ({new_box['X_coordinate']}, {new_box['Y_coordinate']})")
#         print()

#     return coord


# from map import local_location

# local_location()





# from database import reserved_collection_name

# reserved_collection_name.insert_one({"_id": "local_locations" , 'locations' : []})
# print('database created')







# import random

# def local_location(setts, local_height1=225, local_height2=425):
#     local_breath = 175
#     servers_list = []
#     local_coordinates = []

#     for _ in range(setts):
#         y_coordinate_1 = random.randint(75, local_height1 if _ % 2 == 0 else local_height2)
#         x_coordinate_1 = random.randint(75, local_breath)

#         # Calculate the boundary and inside coordinates
#         boundary_coordinates = []
#         inside_coordinates = []

#         # Calculate the square coordinates
#         for y in range(y_coordinate_1 - 50, y_coordinate_1 + 51):
#             for x in range(x_coordinate_1 - 50, x_coordinate_1 + 51):
#                 if (
#                     y in [y_coordinate_1 - 50, y_coordinate_1 + 50]
#                     or x in [x_coordinate_1 - 50, x_coordinate_1 + 50]
#                 ):
#                     boundary_coordinates.append((y, x))
#                 else:
#                     inside_coordinates.append((y, x))

#         local_coordinate = {
#             'boundary_coordinates': boundary_coordinates,
#             'inside_coordinates': inside_coordinates
#         }

#         local_coordinates.append(local_coordinate)

#     # Print the generated coordinates
#     for i, coordinates in enumerate(local_coordinates):
#         print(f"Set {i + 1} Coordinates:")
#         print("Boundary Coordinates:")
#         for coord in coordinates['boundary_coordinates']:
#             print(coord)
#         print("Inside Coordinates:")
#         for coord in coordinates['inside_coordinates']:
#             print(coord)
#         print()

# Call the function with the desired number of sets
# local_location(1)




##This code was used for generating the matrix for the map

# import numpy as np
# import os

# # Define the dimensions of the array
# rows = 5000
# cols = 10000

# # Create the array of zeros
# array = np.zeros((rows, cols))
# array[0, :] = np.arange(cols)
# array[:, 0] = np.arange(rows)

# # Check if the file map.txt exists
# if os.path.exists("map.txt"):
#     # If the file exists, rewrite it with the data from the array
#     with open("map.txt", "w") as file:
#         np.savetxt(file, array, delimiter=" ", fmt="%d")
#         print("File has been created")
# else:
#     # If the file doesn't exist, create it and dump the data into it
#     with open("map.txt", "w") as file:
#         np.savetxt(file, array, delimiter=" ", fmt="%d")
#         print("data has been enterd")

# Read the data from the map.txt file into an array
# array = np.loadtxt("map.txt")

# # Retrieve the value at position (4500, 5000)
# array[]

# import numpy as np
# import os

# def generate_and_update_matrix(file_path):
#     # Define the dimensions of the array
#     rows = 5000
#     cols = 10000

#     # Create the array of zeros
#     array = np.zeros((rows, cols))
#     array[0, :] = np.arange(cols)
#     array[:, 0] = np.arange(rows)

#     # Generate a square matrix of 50x50 with random center coordinates
#     matrix_size = 50
#     center_x = np.random.randint(50, cols - 50)
#     center_y = np.random.randint(50, rows - 50)

#     # Update the values in the array with the new matrix
#     array[center_y - matrix_size//2:center_y + matrix_size//2, center_x - matrix_size//2:center_x + matrix_size//2] = np.arange(matrix_size * matrix_size).reshape(matrix_size, matrix_size)

#     # Save the updated matrix to the file
#     with open(file_path, "w") as file:
#         np.savetxt(file, array, delimiter=" ", fmt="%d")

#     print("Matrix has been updated and saved to", file_path)

# # Specify the file path
# file_path = "E:\\Onepiecebot\\map.txt"

# # Call the function to generate and update the matrix
# generate_and_update_matrix(file_path)









# import numpy as np
# import os

# def generate_and_update_matrix(file_path):
#     # Define the dimensions of the array
#     rows = 500
#     cols = 1000

#     # Create the array of zeros
#     array = np.zeros((rows, cols), dtype='<U1')  # Use dtype='<U1' to store single-character strings

#     # Generate a random center point within the specified ranges
#     center_x = np.random.randint(100, 900)
#     center_y = np.random.randint(100, 400)

#     # Update the values in the array to create a 50x50 square centered at the random point
#     matrix_size = 50
#     array[center_y - matrix_size//2:center_y + matrix_size//2, center_x - matrix_size//2:center_x + matrix_size//2] = '*'

#     # Save the updated matrix to the file
#     with open(file_path, "w") as file:
#         np.savetxt(file, array, delimiter=" ", fmt="%s")

#     print("Matrix has been updated and saved to", file_path)

# # Specify the file path
# file_path = "E:\\Onepiecebot\]map.txt"

# # Call the function to generate and update the matrix
# generate_and_update_matrix(file_path)




# import numpy as np
# import random
# from database import reserved_collection_name
# from shapely.geometry import Point
# from shapely.ops import cascaded_union



# # Load the existing matrix from a file
# existing_matrix = np.loadtxt("E:\\Onepiecebot\\map.txt", dtype=str)

# # Generate coordinates using the local_location() function and update the matrix
# def update_matrix_with_coordinates(matrix):
#     generated_coordinates = []
    
#     # Create a buffer around the previously generated coordinates
#     buffer_distance = 150  # will be giving it a range in the future
#     buffer_polygons = [Point(coord).buffer(buffer_distance) for coord in generated_coordinates]
#     buffer_union = cascaded_union(buffer_polygons)

#     # Generate coordinates until unique coordinates are found
#     while True:
#         x_coordinate = random.randint(0, matrix.shape[1]-1)
#         y_coordinate = random.randint(0, matrix.shape[0]-1)
#         new_coordinate = (x_coordinate, y_coordinate)

#         # Check if coordinates already exist in the buffer
#         if buffer_union is None or not buffer_union.contains(Point(new_coordinate)):
#             break

#     # Add the new coordinates to the list
#     generated_coordinates.append(new_coordinate)

#     # Update the matrix with the generated coordinates
#     matrix[y_coordinate:y_coordinate+50, x_coordinate:x_coordinate+50] = " "

#     return new_coordinate


# # Call the local_location function to generate and update the matrix
# new_coordinate = update_matrix_with_coordinates(existing_matrix)

# # Store the new coordinate in the MongoDB collection
# try:
#     reserved_collection_name.update_one(
#         {"_id": "local_locations"},
#         {"$push": {"locations": new_coordinate}}
#     )
# except Exception as e:
#     print(f"Error storing coordinates in MongoDB: {str(e)}")

# # Save the updated matrix to the same file
# file_path = "E:\\Onepiecebot\\map.txt"
# with open(file_path, "w") as file:
#     np.savetxt(file, existing_matrix, delimiter=" ", fmt="%s")

# print("Matrix has been updated and saved to", file_path)




# import numpy as np
# import os

# # Define the dimensions of the array
# rows = 501  # 0 to 500 inclusive
# cols = 1001  # 0 to 1000 inclusive

# # Create the array of zeros
# array = np.zeros((rows, cols))

# # Fill the first row with column indices
# array[0, :] = np.arange(cols)

# # Fill the first column with row indices
# array[:, 0] = np.arange(rows)

# # Check if the file map.txt exists
# if os.path.exists("map.txt"):
#     # If the file exists, rewrite it with the data from the array
#     with open("map.txt", "w") as file:
#         np.savetxt(file, array, delimiter="\t", fmt="%d")
#         print("File has been updated")
# else:
#     # If the file doesn't exist, create it and dump the data into it
#     with open("map.txt", "w") as file:
#         np.savetxt(file, array, delimiter="\t", fmt="%d")
#         print("File has been created")

# print("Matrix saved to map.txt")








# from database import reserved_collection_name as rc

# coordinates =  rc.find_one({"_id":"local_locations"})

# coordinate = coordinates['locations'][0]

# print(coordinate)

# from database import reserved_collection_name as rc
# import numpy as np

# def design_map(file_path='E:\\onepiece_bot\\map.txt'):

#         coordinatess =  rc.find_one({"_id":"local_locations"})

#         coordinates = coordinatess['locations'][0]

#         # Load the existing matrix from the file
#         array = np.loadtxt(file_path)
    
#         # Iterate over the coordinates and update the matrix
#         for coordinate in coordinates:
#             x = coordinate['X_coordinate']
#             y = coordinate['Y_coordinate']
#             matrix_size = 50
    
#             # Update the values in the array with the new coordinates
#             array[y - matrix_size//2:y + matrix_size//2, x - matrix_size//2:x + matrix_size//2] = np.arange(matrix_size * matrix_size).reshape(matrix_size, matrix_size)
    
#         # Save the updated matrix to the file
#         np.savetxt(file_path, array, delimiter="\t", fmt="%d")
    

# from database import reserved_collection_name as rc
# import numpy as np
# def design_map():
    # collection = rc.find_one({"_id": "local_locations"})
    # coordinates = collection['locations'][-1]
    

    
    # # Find the maximum X and Y coordinates to determine the dimensions of the matrix
    # max_x = max(coordinate['X_coordinate'] for coordinate in local_coordinates_list)
    # max_y = max(coordinate['Y_coordinate'] for coordinate in local_coordinates_list)
    
    
    # # Create an empty matrix of zeros with dimensions (max_y + 1) x (max_x + 1)
    # matrix = np.zeros((max_y + 1, max_x + 1), dtype=int)
    
    # # Iterate over the local coordinates and update the matrix with the index values
    # for i, coordinate in enumerate(local_coordinates_list):
    #     x = coordinate['X_coordinate']
    #     y = coordinate['Y_coordinate']
    #     matrix[y, x] = i + 1
    
    # np.savetxt('sample.txt', matrix, delimiter="\t", fmt="%d")


# design_map()



# import numpy as np # import the NumPy library

# matrix = np.loadtxt("matrix_map.txt", dtype=str, delimiter=" ", skiprows=1) # load the matrix from the txt file using NumPy
# np.savetxt("matrix_map.txt", matrix, fmt="%4s", delimiter=" ") # save the modified matrix back to the txt file using NumPy


# from database import reserved_collection_name as rc
# import numpy as np

# def design_map(file_path='.\matrix_map.txt'):

#         coordinatess =  rc.find_one({"_id":"local_locations"})

#         coordinates = coordinatess['locations'][0]

#         # Load the existing matrix from the file
#         array = np.loadtxt(file_path)
    
#         # Iterate over the coordinates and update the matrix
#         for coordinate in coordinates:
#             x = coordinate['X_coordinate']
#             y = coordinate['Y_coordinate']
#             matrix_size = 50
    
#             # Update the values in the array with the new coordinates
#             array[y - matrix_size//2:y + matrix_size//2, x - matrix_size//2:x + matrix_size//2] = np.arange(matrix_size * matrix_size).reshape(matrix_size, matrix_size)
    
#         # Save the updated matrix to the file
#         np.savetxt(file_path, array, delimiter="\t", fmt="%d")

# design_map()







from PIL import Image, ImageDraw

# Define the dimensions of the map
width = 50
height = 50

# Create a blank image with a white background
map_image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(map_image)

# Draw the market (0-30 in x axis, 0-20 in y axis)
for x in range(31):
    for y in range(21):
        map_image.putpixel((x, y), (255, 0, 0))  # Red color

# Draw the port (0-30 in x axis, 20-49 in y axis)
for x in range(31):
    for y in range(21, 50):
        map_image.putpixel((x, y), (135, 206, 235))  # Sky blue color

# Draw the town (30-45 in x axis, 0-50 in y axis)
for x in range(31, 46):
    for y in range(50):
        map_image.putpixel((x, y), (0, 128, 0))  # Green color

# Draw the army camp (45-50 in x axis, 0-25 in y axis)
for x in range(46, 50):
    for y in range(26):
        map_image.putpixel((x, y), (0, 100, 0))  # Dark green color

# Draw the palace (45-50 in x axis, 25-50 in y axis)
for x in range(46, 50):
    for y in range(26, 50):
        map_image.putpixel((x, y), (128, 0, 128))  # Purple color

# Add gaps between the boundaries
gap_width = 2

# Gap between market and port
for x in range(31 - gap_width, 31 + gap_width + 1):
    for y in range(21 - gap_width, 50 + gap_width + 1):
        if not (31 <= x <= 45 and 21 <= y <= 25):
            draw.point((x, y), fill="black")

# Gap between market and town
for x in range(31 - gap_width, 46 + gap_width + 1):
    for y in range(21 - gap_width, 50 + gap_width + 1):
        if not (31 <= x <= 45 and 21 <= y <= 25):
            draw.point((x, y), fill="black")

# Gap between town and port
for x in range(31 - gap_width, 31 + gap_width + 1):
    for y in range(21 - gap_width, 50 + gap_width + 1):
        if not (31 <= x <= 45 and 21 <= y <= 25):
            draw.point((x, y), fill="black")

# Gap between town and army camp
for x in range(31 - gap_width, 46 + gap_width + 1):
    for y in range(21 - gap_width, 26 + gap_width + 1):
        if not (31 <= x <= 45 and 21 <= y <= 25):
            draw.point((x, y), fill="black")

# Gap between town and palace
for x in range(31 - gap_width, 46 + gap_width + 1):
    for y in range(21 - gap_width, 26 + gap_width + 1):
        if not (31 <= x <= 45 and 21 <= y <= 25):
            draw.point((x, y), fill="black")

## Gap between palace and army camp
for x in range(46 - gap_width, 50 + gap_width + 1):
    for y in range(26 - gap_width, 50 + gap_width + 1):
        if not (31 <= x <= 45 and 21 <= y <= 25):
            draw.point((x, y), fill="black")

# Add roads in the gaps
road_width = 3

# Road between market and port
for x in range(31 - gap_width - road_width // 2, 31 + gap_width + road_width // 2 + 1):
    for y in range(21 - gap_width - road_width // 2, 50 + gap_width + road_width // 2 + 1):
        if not (31 <= x <= 45 and 21 <= y <= 25):
            map_image.putpixel((x, y), (255, 255, 0))  # Yellow color

# Road between market and town
for x in range(31 - gap_width - road_width // 2, 46 + gap_width + road_width // 2 + 1):
    for y in range(21 - gap_width - road_width // 2, 50 + gap_width + road_width // 2 + 1):
        if not (31 <= x <= 45 and 21 <= y <= 25):
            map_image.putpixel((x, y), (255, 255, 0))  # Yellow color

# Road between town and port
for x in range(31 - gap_width - road_width // 2, 31 + gap_width + road_width // 2 + 1):
    for y in range(21 - gap_width - road_width // 2, 50 + gap_width + road_width // 2 + 1):
        if not (31 <= x <= 45 and 21 <= y <= 25):
            map_image.putpixel((x, y), (255, 255, 0))  # Yellow color

# Road between town and army camp
for x in range(31 - gap_width - road_width // 2, 46 + gap_width + road_width // 2 + 1):
    for y in range(21 - gap_width - road_width // 2, 26 + gap_width + road_width // 2 + 1):
        if not (31 <= x <= 45 and 21 <= y <= 25):
            map_image.putpixel((x, y), (255, 255, 0))  # Yellow color

# Road between town and palace
for x in range(31 - gap_width - road_width // 2, 46 + gap_width + road_width // 2 + 1):
    for y in range(21 - gap_width - road_width // 2, 26 + gap_width + road_width // 2 + 1):
        if not (31 <= x <= 45 and 21 <= y <= 25):
            map_image.putpixel((x, y), (255, 255, 0))  # Yellow color

# Road between palace and army camp
for x in range(46 - gap_width - road_width // 2, 50 + gap_width + road_width // 2 + 1):
    for y in range(26 - gap_width - road_width // 2, 50 + gap_width + road_width // 2 + 1):
        if not (31 <= x <= 45 and 21 <= y <= 25):
            map_image.putpixel((x, y), (255, 255, 0))  # Yellow color

# Save the map image
map_image.save("map.png")

