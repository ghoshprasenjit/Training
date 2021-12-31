import os
from datetime import datetime

##Get all methods of os
# print(dir(os))

##current_directory_path
# current_directory_path = os.getcwd()
#print(current_directory_path)

## cnange_directory
# os.chdir('C:\Projects')

##list of file and folder of a directory
# print(os.listdir())

##Create a new folder in a directory
# os.mkdir('test folder')

##Create nasted folders in a directory
# os.makedirs('Folder1/nasted folder1')

##Remove a new folder from a directory
# os.rmdir('test folder')

##Remove nasted folders from a directory
# os.removedirs('Folder1/nasted folder1')

##Rename File
#os.rename('demo.txt','test.txt')

##File Info
# print(os.stat('test.txt'))
# print(os.stat('test.txt').st_size) #File Size in byte

##File Last Modified
# time_data = os.stat('test.txt').st_mtime
# print(datetime.fromtimestamp(time_data))

##Wolk with Directory Tree
# for dirpath, dirnames, filenames in os.walk('C:\Projects\Test'):
#     print('dirpath', dirpath)
#     print('dirnames', dirnames)
#     print('filenames', filenames)
#     print()

##Get Environment Veriables
# print(os.environ.get('USERNAME'))

##OS Path join folder and file
# print(os.path.join(os.getcwd(),'test.txt'))

## OS Path Extracr file name from a Path
# print(os.path.basename(r'C:\Projects\Test\Test Py\test.txt'))


## OS Path Extracr Directory name from a Path
# print(os.path.dirname(r'C:\Projects\Test\Test Py\test.txt'))

## OS Path Extracr file and Directory name from a Path
# print(os.path.split(r'C:\Projects\Test\Test Py\test.txt'))

## Check Directory Exist or Not
# print(os.path.exists(r'C:\Projects\Test\Test Py\test1.txt'))

## Check IS File
# print(os.path.isfile(r'C:\Projects\Test\Test Py.txt'))

## Check IS Directory
# print(os.path.isdir(r'C:\Projects\Test\Test Py'))

## Get File Extention
print(os.path.splitext(r'C:\Projects\Test\Test Py\test1.txt'))


#print(os.listdir())