#Importing the class Path from the module pathlib
from pathlib import Path
#Importing the module Image from the PIL library
from PIL import Image

#We create the path to our images folder
#And save it in a variable imgs_path
#Path.cwd() returns the current working directory
#where the program .py file is.
input_path = Path.cwd()/Path('input')
output_path = Path.cwd()/Path('output')

#We use here the method glob to search for the .png files
for x in input_path.glob('*.png'):
    #This with statement is not necessary but is used to ensure
    #the Image will be closed
    with Image.open(x) as im2:
        #x.stem returns the name of the file and we add the .jpg extension
        save_file_name = x.stem+'.jpg'
        #Create the path for the saved file
        save_path = output_path / save_file_name
        #We need to conver the image opened to RGB
        rgb_im2 = im2.convert('RGB')
       #Save the image with the path created before
        #We have pass the % of quality we want for the .jpg
        rgb_im2.save(save_path, quality=95)
        
print("All images converted")
