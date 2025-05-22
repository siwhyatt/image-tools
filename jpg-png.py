#Convert JPG to PNG
from pathlib import Path
from PIL import Image
from itertools import chain

cwd = Path.cwd()

for x in chain(cwd.glob('*.jpg'), cwd.glob('*.jpeg')):

    with Image.open(x) as img:

        save_file_name = x.stem+'.png'

        save_path = cwd / save_file_name

        img.save(save_path)
        
print("All images converted")
