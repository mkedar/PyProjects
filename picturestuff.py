import PIL
import math
from PIL import Image, ImageStat


gscale =  " ░▒▓█"
gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
gscale2 = '@%#*+=-:. '
counter = 255/5
img = Image.open("wp3457512.jpg")
basewidth = 75
wpercent = (basewidth / float(img.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
img = img.resize((basewidth, hsize), Image.ANTIALIAS)
img = img.convert('LA')
img.save('nessbl2.png')
width, height = img.size
stat = ImageStat.Stat(img)
avg = stat.mean[0]
def get_image_text(num):
    return gscale[math.floor(num/counter)]
for r in range(height):
    print()
    for c in range(width):
        r1, g1 = img.getpixel((c , r ))
        stuff = get_image_text(r1)
        print(stuff, end=' ')
