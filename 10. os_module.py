from fileinput import filename
import os

# dir shows what variables and functions the module holds
print(dir(os))

# 1. Get current working directory
print(os.getcwd())

# 2. Change current working directory
os.chdir('K:/DSA/CoreySchafer-PythonCourse/')

# 3. List items in directory
print(os.listdir())

# 4. Create folder
os.mkdir('FolderTest')
os.makedirs('FolderTest2/SubDir2')

# 5. Delete folder
os.rmdir('FolderTest2')
os.removedirs('FolderTest2/SubDir2') # Caution! - This recursively deletes the directory and sub-directories specified.

# 6. Rename file
os.rename('demo.txt','test.txt')

# 7. Get information about file
print(os.stat('test.txt').st_size)

from datetime import datetime
mod_time = os.stat('test.txt').st_mtime
print(datetime.fromtimestamp(mod_time))

# 8. See entire directory tree and see files within it
"""
    Generator which yields tuple of 3 values
    1. Directory path
    2. Directories within that path
    3. Files within that path
"""
os.walk() #does not work, as it is a three value tuple

print('--------------------------------')
for dirpath, dirnames, filenames in os.walk('./'):    
    print('Current Path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames)
    print('--------------------------------')

# 9. To access environment variable
os.environ.get('USERPROFILE')

# 10. Create a new file in a specified path from env variable
# Way - 1
file_path = os.environ.get('USERPROFILE') + 'test.txt'
print(file_path) # You could see, this is error prone as we missed slash '/' in between

# Way - 2
file_path = os.path.join(os.environ.get('USERPROFILE'), 'test.txt')
print(file_path)

# 11. Getting info from path specified
print(os.path.basename('/tmp/dir/test.txt')) # To get file name
print(os.path.dirname('/tmp/dir/test.txt')) # To get path excluding file name
print(os.path.split('/tmp/dir/test.txt')) # To get both in a tuple
print(os.path.exists('/tmp./test.txt')) # To check existance of directory or file
print(os.path.isdir('./modules/my_module')) # To verify if it's a directory (when extension is not given)
print(os.path.isfile('./modules/my_module.py')) # To verify if it's a file (extension should be specified)
print(os.path.splitext('/modules/my_module.py')) # Splits file root and extension

print(dir(os.path)) # To see the full list of things you can do with path