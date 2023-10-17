import os
import cv2
import numpy as np

# Get the list of image files in the folder
folder_path = input("Path/to/folder ")

image_files = [f for f in os.listdir(folder_path) if f.endswith(".jpg") or f.endswith(".png")]

# Loop through each image file and resize it
for file_name in image_files:

    #x.stem returns the name of the file without the extension
    save_file_name = os.path.splitext(file_name)

    # Open the image file
    image = cv2.imread(os.path.join(folder_path, file_name))

    # Convert the image to grayscale
    image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)

    # Get the height and width of the image
    height, width, channels = image.shape

    # Define the white color threshold (adjust as needed)
    white_threshold = 200
    black_threshold = 100

    # Loop through each pixel in the grayscale image
    for y in range(height):
        for x in range(width):
            # Get the pixel value at (x, y)
            pixel_value = image[y, x][0]
            
            # Check if the pixel is white
            if pixel_value > white_threshold:
                # Set the pixel to black
                image[y, x] = [0, 0, 0, 255]  # BGR color for black

            if pixel_value < black_threshold:
                # Set the pixel to black
                image[y, x] = [255, 255, 255, 0]  # BGR color for white

    # Save the resized image with a new filename
    new_file_name = "black_" + save_file_name[0] + ".png"
    cv2.imwrite(new_file_name, image)
