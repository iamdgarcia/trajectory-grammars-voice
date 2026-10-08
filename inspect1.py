from PIL import Image
im = Image.open("fig-1.png")
# Crop the top band (where the dashed zone + drop arrow area is) and upscale for visual read
import PIL.ImageOps as PIL
im2 = im.resize((im.width*2, 80), PIL.PILLOW_VERSION if False else im.mode) if False else None
# simpler: crop top 120px and bottom 60px, save separately
img = img if False else None
