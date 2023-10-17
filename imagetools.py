import os, sys
from PIL import Image


'''
# Open the image file
image = Image.open("r4.jpg")

# Get the current width and height
width, height = image.size

# Calculate the new height based on the desired width
new_width = 1200
new_height = int((height / width) * new_width)

# Resize the image
resized_image = image.resize((new_width, new_height))

# Save the resized image
resized_image.save("r4.jpg")

'''

# Set the desired width of the resized images
new_width = input("New width in pixels: ")

# Get the list of image files in the folder
folder_path = "./imgs"
image_files = [f for f in os.listdir(folder_path) if f.endswith(".jpg")]

# Loop through each image file and resize it
for file_name in image_files:
    # Open the image file
    image = Image.open(os.path.join(folder_path, file_name))

    # Get the current width and height
    width, height = image.size

    # Calculate the new height based on the desired width
    new_height = int((height / width) * new_width)

    # Resize the image
    resized_image = image.resize((new_width, new_height))

    # Save the resized image with a new filename
    new_file_name = "resized_" + file_name
    resized_image.save(os.path.join(folder_path, new_file_name))



