import json
import os

# Function to rename images based on JSON data
def rename_images(json_file, image_folder):
    # Load the JSON file
    with open(json_file, 'r') as file:
        data = json.load(file)

    # Iterate over the items in the JSON data
    for icon_name, item_id in data.items():
        # Construct the current image name and the new image name
        current_image_name = f"{icon_name}.webp"
        new_image_name = f"{item_id}.webp"
        
        # Construct the full path to the current and new image names
        current_image_path = os.path.join(image_folder, current_image_name)
        new_image_path = os.path.join(image_folder, new_image_name)
        
        # Check if the current image exists
        if os.path.exists(current_image_path):
            # Check if the new image name does not exist
            if not os.path.exists(new_image_path):
                # Rename the image
                os.rename(current_image_path, new_image_path)
                print(f"Renamed {current_image_name} to {new_image_name}")
            else:
                print(f"Cannot rename {current_image_name} to {new_image_name} because the file already exists.")
        else:
            print(f"Image {current_image_name} not found.")

    print('Image renaming process completed.')

# Specify the JSON file and the folder where the images are stored
json_file = 'alldat.json'
image_folder = 'webp'

# Call the function to start renaming images
rename_images(json_file, image_folder)
