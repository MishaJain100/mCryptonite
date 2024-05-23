from PIL import Image
import numpy as np
import os

file_names = ["C:\\Users\\misha\\Downloads\\scrambled2.png", "C:\\Users\\misha\\Downloads\\scrambled1.png"]
img_data = [np.asarray(Image.open(f'{name}')) for name in file_names]

data = img_data[0].copy() + img_data[1].copy()

new_image = Image.fromarray(data)
new_image.save("out.png", "PNG")