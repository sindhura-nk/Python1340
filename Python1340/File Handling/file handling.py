import os
# What is File Handling? Why is it required?

# How to create files => using xs

# How to open the files

# How to read files? => using read(),readline(),readlines()

os.chdir(r"E:\Sindhura\DataSets")
with open("FH-sampledata.txt",'r') as file:
    r1 = file.read()
    print(f"Read():{r1}")
with open("FH-sampledata.txt",'r') as file:
    r2 = file.readline()
    print(f"Readline():{r2}")
with open("FH-sampledata.txt",'r') as file:
    r3 = file.readlines()
    print(f"Readlines():{r3}")

# hint while reading the data: hint represents number of bytes 

with open("FH-sampledata.txt",'r') as file:
    r1 = file.read(20)
    print(f"Read():{r1}")
with open("FH-sampledata.txt",'r') as file:
    r2 = file.readline(20)
    print(f"Readline():{r2}")
with open("FH-sampledata.txt",'r') as file:
    r3 = file.readlines(1000)
    print(f"Readlines():{r3}")





# How to write to files? => using write(),writelines()

# How to append data to existing files: => using write() and choosing 'a' as the mode


# How to close the files

# With clause: why and advantages

# remove a file

# create directory(folder)

# remove directory (os.rmdir removes only an empty directory)

# change the directory path

# create a file within the directory

# change the directory path

# try to remove the directory where you have created a new file

# read an image file : mode = 'rb'

# Problem Statement: write a program that accepts a string from the user and writes it to a text file. 
# Thereafter, the same program reads the text file and displays it on the screen.

print("Seek and Tell methods")
# seek() and tell()
# If we want to get the position of the fileobject
with open("FH-sampledata.txt",'+r') as file:
    data = file.read()
    print(f"Initial position of the file object is : {file.tell()}")
    file.seek(0)
    print(f"Now the file object is at the beginning of the file: {file.tell()}")
    file.seek(10)
    print(f"Initial position of the file object is : {file.tell()}")