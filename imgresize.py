import os
from PIL import Image

# Get the list of image files in the folder
input_folder_path = "input/"
output_folder_path = "output/"

# Get the desired width of the resized images from user input
while True:
    try:
        new_width = int(input("Enter the desired width of the resized images: "))
        break
    except ValueError:
        print("Invalid input. Please enter an integer value.")

width_string = str(new_width)


image_files = [f for f in os.listdir(input_folder_path) if f.endswith(".jpg")]

# Loop through each image file and resize it
for file_name in image_files:
    # Open the image file
    image = Image.open(os.path.join(input_folder_path, file_name))

    # Get the current width and height
    width, height = image.size

    # Calculate the new height based on the desired width
    new_height = (height * new_width) // width

    # Height as string
    height_string = str(new_height)

    # Resize the image
    resized_image = image.resize((new_width, new_height))

    # Save the resized image with a new filename
    new_file_name = "resized_" + width_string + "_x_" + height_string + "_px_" + file_name
    resized_image.save(os.path.join(output_folder_path, new_file_name))



'''
print("Shrink images in the folder")
folder = input("folder: ")
new_width = int(input("width: "))

for i in os.listdir(folder):
    file = f"{folder}/{i}"
    im = Image.open(file)
    #Calculate the new height in relation to the original height
    height_percent = (new_width / float(im.size[1]))
    #Apply that % to calculate the new width
    new_height = int((float(im.size[0])*float(height_percent)))
    #Resize with the new values
    #We use BICUBIC because is a good balance between quality and
    #performance
    im.resize((new_width, new_height))
    im.save(file)
    
'''


'''
#We use here the method glob to search for the .png files
for x in imgs_path.glob('*.jpg'):
    #This with statement is not necessary but is used to ensure
    #the Image will be closed
    with Image.open(x) as im2:
        #Now we need to modify the width in the same proportion as the #height.
        #Calculate the new height in relation to the original height
        height_percent = (new_height / float(im.size[1]))
        #Apply that % to calculate the new width
        new_width = int((float(im.size[0])*float(height_percent)))
        #Resize with the new values
        #We use BICUBIC because is a good balance between quality and
        #performance
        im.resize((new_width, new_height), PIL.Image.BICUBIC).save("bulb2.png")
        
print("All images converted")
'''
