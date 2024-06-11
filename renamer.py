import json
import os

# Load the JSON file
with open('alldat.json', 'r') as file:
    data = json.load(file)

# Specify the folder where the images are stored
image_folder = '\webp'

# Iterate over the items in the JSON data
for icon_name, item_id in data.items():
    # Construct the current image name and the new image name
    current_image_name = f"{icon_name}.webp"
    new_image_name = f"{item_id}.webp"
    
    # Construct the full path to the current and new image names
    current_image_path = os.path.join(image_folder, current_image_name)
    new_image_path = os.path.join(image_folder, new_image_name)
    
    # Check if the current image exists and if the new image name does not exist
    if os.path.exists(current_image_path) and not os.path.exists(new_image_path):
        # Rename the image
        os.rename(current_image_path, new_image_path)
        print(f"Renamed {current_image_name} to {new_image_name}")
    elif os.path.exists(new_image_path):
        print(f"Cannot rename {current_image_name} to {new_image_name} because the file already exists.")
    else:
        print(f"Image {current_image_name} not found.")

print('Image renaming process completed.')
