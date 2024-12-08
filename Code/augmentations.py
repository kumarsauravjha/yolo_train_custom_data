#%%
import cv2
import glob
import os
from PIL import Image, ImageOps
import numpy as np
# %%
path = "D:\\STUDY\\MS\\DATS 6450 Computer Vision\\group assignment\\all_images"
# %%
image_files = glob.glob(f"{path}/*.png") + \
              glob.glob(f"{path}/*.bmp") + \
              glob.glob(f"{path}/*.webp") + \
              glob.glob(f"{path}/*.tiff")

#%%
output_dir = os.path.join(path, "og")
os.makedirs(output_dir, exist_ok=True)
# %%
# %%
counter = 0
for file_path in image_files:
    # print(file_path)
    pil = Image.open(file_path).convert('RGB')
    # pil_new = ImageOps.flip(ImageOps.mirror(pil))
    pil.save(os.path.join(output_dir, f"original_image_{counter}.jpeg"))
    counter += 1
# %%
