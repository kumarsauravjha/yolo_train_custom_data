#%%
import os
import shutil
import random


# %%
images_dir = "D:/STUDY/MS/DATS 6450 Computer Vision/group assignment/yolo_images"
labels_dir = "D:/STUDY/MS/DATS 6450 Computer Vision/group assignment/yolo_labels"
# %%
for folder in ['images/train','images/val','images/test', 'labels/train','labels/val', 'labels/test']:
    os.makedirs(f"Dataset/{folder}", exist_ok=True)

    

# %%
image_files = [f for f in os.listdir(images_dir) if f.endswith(('.jpeg', '.jpg'))]
# %%
random.shuffle(image_files)
train_split = int(0.7* len(image_files))
val_split = int(0.9 * len(image_files))

# %%
train_files = image_files[:train_split]
val_files = image_files[train_split:val_split]
test_files = image_files[val_split:]


# %%
def copy_files(files, image_dest, label_dest):
    for file in files:
        image_path = os.path.join(images_dir, file)
        print(image_path)
        label_path = os.path.join(labels_dir, file.replace('.jpeg', '.txt'))
        print(label_path)
        if os.path.exists(label_path):
            shutil.copy(image_path, image_dest)
            shutil.copy(label_path, label_dest)
            # break


copy_files(train_files, "Dataset/images/train", "Dataset/labels/train")
copy_files(val_files, "Dataset/images/val", "Dataset/labels/val")
copy_files(test_files, "Dataset/images/test", "Dataset/labels/test")

print("Dataset split completed")
# %%
