from PIL import Image, ImageDraw

# create a black square of dimension 50 x 50
img = Image.new("RGB", (50, 50), (0, 0, 0))
draw = ImageDraw.Draw(img)

# define the places and their coordinates
places = {
    "market": [(0,0), (20,0), (0,20), (20,20)],
    "port": [(0,20), (20,20), (0,50), (20,50)],
    "town": [(20,0), (40,0), (20,50), (40,50)],
    "palace": [(40,20), (40,30), (50,20), (50,30)]
}

# define the colors for each place
colors = {
    "market": (255, 255, 0),
    "port": (0, 255, 255),
    "town": (255, 0, 255),
    "palace": (255, 165, 0)
}

# draw each place on the image
for place in places:
    draw.polygon(places[place], fill=colors[place])

# save the image
img.save("map.png")
