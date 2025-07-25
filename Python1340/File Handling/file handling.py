'''
x - create a file

w - add contents to the file: (doesn't exist- file creation)

a - update contents (add new content to the file):  (doesn't exist- file creation)

r - read the contents of the file
'''

import os
# What is File Handling? Why is it required?

# How to create files => using x
# Syntax: f1 = open(file_name,mode)

#f1= open("sampletext2.txt","x")

# How to open the files
# using open method,Syntax: f1 = open(file_name,mode)

# How to read files? => using read(),readline(),readlines()
f2 = open("sample.txt","r")
print(f2.read())
f2.close()


os.chdir(r"E:\Sindhura\DataSets")
with open("FH-sampledata.txt",'r') as file:
    r1 = file.read()
    print(f"Read():{r1}")
with open("FH-sampledata.txt",'r') as file:
    r2 = file.readline()
    print(f"Readline():{r2}")
with open("FH-sampledata.txt",'r') as file:
    r3 = file.readlines()
    print(f"3rd and 5th Line using readlines() :{r3[2]},{r3[4]}")
    print(f"Readlines():{r3}")

#hint while reading the data: hint represents number of bytes 

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
f3 = open("sample.txt","w")
f3.write("Welcome to the Python session.")
f3.close()


# How to append data to existing files: => using write() and choosing 'a' as the mode
f4 = open("sample.txt","a")
f4.write(" The session timings are 9:30-11:30am. Session conducted by Sindhura Trainer")
f4.close()

# read the content after updating the data
f5 = open("sample.txt","r")
print(f5.read())
f5.close()

# How to close the files
#using filename.close()

# With clause: why and advantages
''' 
with open(file_name,mode) as file:
    file.read()
'''
with open("sample.txt","r") as file:
    print("With clause output",file.read())

with open("sample.txt","a") as file:
    file.write("\n Today's topic is File Handling")

with open("sample.txt","r") as file:
    print("With clause output",file.read())

# os.getcwd()
os.chdir(r"E:\Sindhura\Sindhura\Data Science-ETLhive\Files\emoji\happy")
with open("ffhq_1740.png","rb") as file:
    print(file.read())

