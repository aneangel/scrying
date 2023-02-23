# Import the Images module from pillow
from PIL import Image

# Open the image by specifying the image path.
size = 2000, 1000

im = Image.open('stitchedOutputProcessed.jpg')

im_resized = im.resize((2000,1000))
im_resized.save('stitchedOutputUpscaled.jpg')


