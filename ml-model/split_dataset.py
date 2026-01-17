import os, shutil, random

source_dir = "C:/model"
target_dir = "C:/model_split"
train_ratio = 0.8

os.makedirs(f"{target_dir}/train", exist_ok=True)
os.makedirs(f"{target_dir}/val", exist_ok=True)

for class_name in os.listdir(source_dir):
    class_path = os.path.join(source_dir, class_name)
    if not os.path.isdir(class_path):
        continue

    images = [f for f in os.listdir(class_path) if f.lower().endswith(".jpg")]
    random.shuffle(images)
    split_idx = int(len(images) * train_ratio)

    train_images = images[:split_idx]
    val_images = images[split_idx:]

    os.makedirs(f"{target_dir}/train/{class_name}", exist_ok=True)
    os.makedirs(f"{target_dir}/val/{class_name}", exist_ok=True)

    for img in train_images:
        shutil.copy(os.path.join(class_path, img), f"{target_dir}/train/{class_name}/{img}")
    for img in val_images:
        shutil.copy(os.path.join(class_path, img), f"{target_dir}/val/{class_name}/{img}")

print("✅ Dataset split complete.")
