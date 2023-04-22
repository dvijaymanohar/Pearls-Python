

import os

print('Absolute path of file:	 ',
      os.path.abspath(__file__))

print('Absolute directoryname: ',
      os.path.dirname(os.path.abspath(__file__)))


pythonfile = 'pathfinding.py'

# if the file is present in current directory,
# then no need to specify the whole location
print("Path of the file..", os.path.abspath(pythonfile))

for root, dirs, files in os.walk(r'C:\Users\670249175\vmd\vmdone\OneDrive\code_base\prac_repo\python\prac'):
    for name in files:

        # As we need to get the provided python file,
        # comparing here like this
        if name == pythonfile:
            print(os.path.abspath(os.path.join(root, name)))
