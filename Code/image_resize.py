#%%
from PIL import Image
import os

image_dir = "Dataset/images/test"
output_dir = "Dataset/images/test_resized"

os.makedirs(output_dir, exist_ok=True)

for file in os.listdir(image_dir):
    if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
        img = Image.open(os.path.join(image_dir, file))
        img = img.resize((416, 416))  # Resize to 416x416
        img.save(os.path.join(output_dir, file))

# %%
