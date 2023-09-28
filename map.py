import random 
from database import reserved_collection_name as rc , collection_name
import numpy as np
from PIL import Image, ImageDraw
import requests
from io import BytesIO





def map_matrix():
        '''In this funtion i am generating a matrxi map for the game so that i can vizualize things in a better way and also to make the game more interesting.'''
        # Define the number of columns and rows
        columns = 5000
        rows = 2500

        # Create an empty list to store the matrix
        matrix = []

        # Loop through each row
        for i in range(rows):
            # Create an empty list to store the row
            row = []
            # Loop through each column
            for j in range(columns):
                # If it is the first row or the first column, add the index value as a string
                if i == 0 or j == 0:
                    row.append(str(i + j))
                # Otherwise, add a dot as a string
                else:
                    row.append(".")
            # Add the row to the matrix
            matrix.append(row)

        # Open a txt file in write mode
        file = open("matrix_map.txt", "w")

        # Loop through each row in the matrix
        for row in matrix:
            # Join the elements of the row with spaces and write them to the file
            # Use rjust to align the strings to the right with a width of 4 characters
            file.write(" ".join([element.rjust(4) for element in row]) + "\n")

        # Close the file
        file.close()





def generate_coordinates(num_points):
    '''In this funtion currently i am trying to generate a coordinate for a matrix and for further i am planning to update this for checking for the gap and to reduce the server cost i will be making it it generate coordinates all at once and store it in the database'''
    for i in range(num_points):
        coordinates = {}
        local_coordinates = []
        x_coordinate_1 = random.randint(75, 900)
        y_coordinate_1 = random.randint(75, 400)

        x_coordinate_2 = x_coordinate_1 + 50 
        y_coordinate_2 = y_coordinate_1

        x_coordinate_3 = x_coordinate_1
        y_coordinate_3 = y_coordinate_1 + 50

        x_coordinate_4 = x_coordinate_2
        y_coordinate_4 = y_coordinate_3
        
        local_coordinates.append({"X_coordinate": x_coordinate_1, "Y_coordinate": y_coordinate_1})
        local_coordinates.append({"X_coordinate": x_coordinate_2, "Y_coordinate": y_coordinate_2})
        local_coordinates.append({"X_coordinate": x_coordinate_3, "Y_coordinate": y_coordinate_3})
        local_coordinates.append({"X_coordinate": x_coordinate_4, "Y_coordinate": y_coordinate_4})
        
        
        coordinates.update(local_coordinates)
    return coordinates

        # boundries = []







        # collection = rc
        # collection.update_one({ "_id": "local_locations"}, {"$push": {"locations": local_coordinates}})










def design_map(server_id,server_name):
    '''In this funtion i am trying to generate a global map for the game so that i can vizualize things in a better way and also to make the game more interesting.
______________________________________________________________________________________________
so far in this funtion i have generated a image for a map on icone but it dosent look that well so and the coordinates of the map are just 500X250 so i am planning to make a bigger whole map and paste the icons on it insted of making 2 sets of coordinates for the game so that i can generate a map for the game.'''


    # As a pending task i will make it update the matrix later on and generate a image of map for now
        
    try:

                    # Fetch the server info from the server_info collection
                    server_info = collection_name.find_one({'_id':server_id})

                    if server_info is not None:
                        # Get the image URL and coordinates
                        server_pfp_url = server_info['guild_pfp']
                        serverX1, serverY1 = server_info['Coordinates'][0]['X_coordinate'], server_info['Coordinates'][0]['Y_coordinate']
                        # nearest_local = server_info['server_coordinate']

                        # Open the first image
                        image1 = Image.open("E:\\onepiece_bot\\IMAGES\\clear_extra.jpg")

                        image11 = Image.open("E:\onepiece_bot\IMAGES\clear.jpg")

                        # Download the server icon image from the URL
                        response = requests.get(server_pfp_url)
                        server_icon = Image.open(BytesIO(response.content))

                        # Calculate the new siy_coordinatee for the server icon image
                        server_icon_new_siy_coordinatee = (int(image11.size[0] * 0.2), int(image11.size[1] * 0.1))




                        # Resiy_coordinatee the server icon image
                        server_icon = server_icon.resize(server_icon_new_siy_coordinatee)
                        server_icon = server_icon.convert("RGBA")
                        # Calculate the position for centering the icon around the dots
                        icon_x_position = serverX1 - server_icon_new_siy_coordinatee[0] // 2
                        icon_y_position = serverY1 - server_icon_new_siy_coordinatee[1] // 2

                        # Paste the server icon image onto the map
                        image1.paste(server_icon, (icon_x_position, icon_y_position), server_icon)

                        # Add lines with unique colors and print dot numbers
                        # draw = ImageDraw.Draw(image1)
                        # dot_siy_coordinatee = 5  # Increased dot siy_coordinatee

                        # # Collect dot coordinates in a list
                        # dot_coordinates = []
                        # for local_square_dict in nearest_local:
                        #     for _, coordinates in local_square_dict.items():
                        #         x = coordinates['y_coordinate']
                        #         y = coordinates['x_coordinate']
                        #         dot_coordinates.append((x, y))

                        # # Draw lines with unique colors and print dot numbers
                        # line_connections = [
                        #     (0, 1),
                        #     (1, 2),
                        #     (2, 4),
                        #     (4, 7),
                        #     (7, 6),
                        #     (6, 5),
                        #     (5, 3),
                        #     (3, 0)
                        # ]

                        # for start, end in line_connections:
                        #     x1, y1 = dot_coordinates[start]
                        #     x2, y2 = dot_coordinates[end]
                            
                        #     line_color = (0, 0, 0, 255)  # Black color
                        #     draw.line([(x1, y1), (x2, y2)], fill=line_color, width=2)  # Increase the line width
                            
                        #     print(f"Line from dot{start} to dot{end}")

                        # Save the modified image
                        image1.save(f"E:\\onepiece_bot\\IMAGES\\global_map.png")




    except Exception as e:
                print(f"An error occurred while generating the map: {e}")



