from collections import Counter
from PIL import Image, ImageDraw


image = Image.open('dirty-img12.jpg')
obj = image.load()
width = image.size[0]
height = image.size[1]

# print(width)
# print(height)

# print(image.getpixel((x,y)))

color = []

white_color = (255,255,255)
black_color = (0,0,0)

for x in range(width):
    for y in range(height):
        r = image.getpixel((x,y))[0]
        g = image.getpixel((x,y))[1]
        b = image.getpixel((x,y))[2]
        # color.append(image.getpixel((x,y)))
        S = r + g + b
        # if S > ((255 // 2) * 3):
        #     image.putpixel((x,y), white_color)
        # else:
        #     image.putpixel((x,y), black_color)
        if S > 600:
            image.putpixel((x,y), white_color)
        else:
            image.putpixel((x,y), black_color)

# c = Counter(color)
#
# print(c)

image.save('recolor1.jpg')

image = Image.open('recolor1.jpg')
obj = image.load()
draw = ImageDraw.Draw(image)
point_start = None

point_end = None

for y in range(height):
    for x in range(width):
        r = image.getpixel((x,y))[0]
        g = image.getpixel((x,y))[1]
        b = image.getpixel((x,y))[2]
        S = r + g + b

        if S == 765 and point_start is None:
            point_start = (x,y)

for x in range(width-1, 0, -1):
    for y in range(height-1, 0, -1):
        # print(x,y)
        # input( )
        r = image.getpixel((x,y))[0]
        g = image.getpixel((x,y))[1]
        b = image.getpixel((x,y))[2]
        S = r + g + b

        if S == 765 and point_end is None:
            point_end = (x,y)

draw.line((point_start, point_end), fill=black_color, width=5)

image.save('recolor2.jpg')
