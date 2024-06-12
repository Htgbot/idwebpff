import json
import os
from shutil import copy2

# Function to rename images based on JSON data and copy them to a new folder
def rename_and_copy_images(json_file, image_folder, new_folder):
    # Load the JSON file
    with open(json_file, 'r') as file:
        data = json.load(file)

    # Create the new folder if it doesn't exist
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)

    # Iterate over the items in the JSON data
    for icon_name, item_id in data.items():
        # Construct the current image name and the new image name
        current_image_name = f"{icon_name}.webp"
        new_image_name = f"{item_id}.webp"
        
        # Construct the full path to the current and new image names
        current_image_path = os.path.join(image_folder, current_image_name)
        new_image_path = os.path.join(new_folder, new_image_name)
        
        # Check if the current image exists
        if os.path.exists(current_image_path):
            # Check if the new image name does not exist in the new folder
            if not os.path.exists(new_image_path):
                # Copy the image to the new folder with the new name
                copy2(current_image_path, new_image_path)
                print(f"Copied {current_image_name} to {new_image_name} in {new_folder}")
            else:
                print(f"Cannot copy {current_image_name} to {new_folder} because {new_image_name} already exists there.")
        else:
            print(f"Image {current_image_name} not found in {image_folder}.")

    print('Image renaming and copying process completed.')

# Specify the JSON file, the folder where the images are currently stored, and the new folder
json_file = 'alldat.json'
image_folder = 'webp'
new_folder = 'webpimg'

# Call the function to start renaming images and copying them to the new folder
rename_and_copy_images(json_file, image_folder, new_folder)
