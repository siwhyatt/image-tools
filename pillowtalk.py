from PIL import Image
import numpy as np

im = Image.open('3.jpg')

data = np.array(im)   # "data" is a height x width x 4 numpy array
red, green, blue, alpha = data.T # Temporarily unpack the bands for readability

# Replace white with red... (leaves alpha values alone...)
white_areas = (red == 255) & (blue == 255) & (green == 255)
data[..., :-1][white_areas.T] = (0, 0, 0) # Transpose back needed

im2 = Image.fromarray(data)
im2.show()
