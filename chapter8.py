#learning log from chapter 8, input and output of files

# 2 key properties: file name and path
# remeber that windows system uses a \ backslash for path
# linux and mac system use a / forward slash for path
# write scripts for both systems for full support

import os

osPath = os.path.join ('user', "bin", "spam") # this creates a path that joins with the system appropriate separator
print ("the os path is " + osPath)

# getting the current working directory

cwdPath = os.getcwd() #.chdir will change the directory
print ("the current working directory path is " + cwdPath)

# relative and absolute path

# absolute path, which always begins with the root folder
# relative path, which is relative to the program’s current working directory

# os.makedirs ("User/hutsunhao/makedirsTest") this will make a directory with respect to the current working directory

