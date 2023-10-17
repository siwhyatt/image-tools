# Convert SVG to PNG

import os
import cairosvg

# Get the list of image files in the folder
folder_path = "imgs/"

image_files = [f for f in os.listdir(folder_path) if f.endswith(".svg")]

# Loop through each image file and resize it
for file_name in image_files:

    #splitext returns tupple of file name and extention
    save_file_name = os.path.splitext(file_name)

    new_file_name = folder_path + save_file_name[0] + ".png"

    # Open the image file
    cairosvg.svg2png(
    file_obj = open(os.path.join(folder_path, file_name), "rb"), write_to = new_file_name)