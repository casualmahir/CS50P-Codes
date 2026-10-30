#Combining two images into an animated GIF with the Pillow library
import sys

from PIL import Image

images = []

#Opening every image passed on the command line
for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

#Saving the first image as a GIF and adding the second as the next frame
images[0].save(
    "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)
