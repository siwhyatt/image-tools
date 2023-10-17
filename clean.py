import os
 
dir = 'input'
for f in os.listdir(dir):
    os.remove(os.path.join(dir, f))
    
print('All input images deleted')

dir = 'output'
for f in os.listdir(dir):
    os.remove(os.path.join(dir, f))
    
print('All output images deleted')
