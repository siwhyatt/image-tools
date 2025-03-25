import os
from PIL import Image
from helpers import GetArgument


# Get the list of image files in the folder
input_folder = os.getcwd()

def GetSize():
    # Get the desired width of the resized images from user input
    while True:
        try:
            new_width = int(input("Enter the desired width of the resized images: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer value.")

    # width_string = str(new_width)

    return new_width

def Rename():
    response = GetArgument("Rename files with new sizes? Y/N: ", 2)

    if response.lower() == "y":
        return True
    else:
        return False

    
def ResizeImages(new_width, folder_path, rename, file_types):

    extensions = {
        "1": [".jpg", ".jpeg", ".png"],  # All supported types
        "2": [".jpg", ".jpeg"],          # Just JPG/JPEG
        "3": [".png"]                    # Just PNG
    }

    selected_extensions = extensions.get(file_types, extensions["1"])

    image_files = [f for f in os.listdir(folder_path)]

    # Loop through each image file and resize it
    for file_name in image_files:
        if any(file_name.lower().endswith(ext) for ext in selected_extensions):
            # Open the image file
            image = Image.open(os.path.join(folder_path, file_name))

            # Get the current width and height
            width, height = image.size

            # Calculate the new height based on the desired width
            new_height = (height * new_width) // width

            # Resize the image
            resized_image = image.resize((new_width, new_height))

            if rename:
                # Save the resized image with a new filename
                width_string = str(new_width)
                height_string = str(new_height)
                new_file_name = "resized_" + width_string + "_x_" + height_string + "_px_" + file_name
                resized_image.save(os.path.join(folder_path, new_file_name))
                print(f"Resized & renamed image: {new_file_name}")
            else:
                # Save the image with same file name
                resized_image.save(os.path.join(folder_path, file_name))
                print(f"Resized image: {resized_image}")


def main():
    new_width = GetSize()
    rename = Rename()
    file_types = GetArgument(
        "Select file types to resize:\n"
        "1. All supported (jpg, jpeg, png)\n"
        "2. JPG/JPEG only\n"
        "3. PNG only\n"
        "Enter choice (1-3): ", 2)
    ResizeImages(new_width, input_folder, rename, file_types)


if __name__ == "__main__":
    main()
