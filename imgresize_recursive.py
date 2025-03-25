import os
from PIL import Image

def resize_image(folder_path, new_width):
    for foldername, subfolders, filenames in os.walk(folder_path):
        for filename in filenames:
            if filename.endswith((".jpg", ".jpeg", ".png")):

                # Open the image file
                image_path = os.path.join(foldername, filename)
                image = Image.open(image_path)

                # Get the current width and height
                width, height = image.size

                # Calculate the new height based on the desired width
                new_height = (height * new_width) // width

                # Resize the image
                resized_image = image.resize((new_width, new_height))

                # Save the resized image with a new filename
                resized_image.save(image_path)
                
                # Confirm resize
                print(f"{image_path} resized to {str(new_width)}x{str(new_height)}")

def main():
    # Get the desired width of the resized images from user input
    while True:
        try:
            new_width = int(input("Enter the desired width of the resized images: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer value.")

    folder_path = os.getcwd()

    resize_image(folder_path, new_width)

if __name__ == "__main__":
    main()
