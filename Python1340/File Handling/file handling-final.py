import os
print("Seek and Tell methods")
# seek() and tell()
# If we want to get the position of the fileobject
os.chdir(r"E:\Sindhura\DataSets")
with open("FH-sampledata.txt",'+r') as file:
    data = file.read()
    print(f"Initial position of the file object is : {file.tell()}")
    file.seek(0)
    print(f"Now the file object is at the beginning of the file: {file.tell()}")
    file.seek(10)
    print(f"New position of the file object is : {file.tell()}")

# create a new directory/folder 
#os.mkdir("dummy") # since the  directory got changed to Datasets folder, this folder gets created in that location
# changing the directory
os.chdir(r"E:\Sindhura\3RI\Python Repository\repository\Python1340")

# create a new directory in the above path
#os.mkdir("dummy")

# remove the folder
#os.rmdir("dummy")

# create a new folder, change the directory and then create a file inside of it
#os.mkdir("dummy")

# os.chdir(r"E:\Sindhura\3RI\Python Repository\repository\Python1340\dummy")

# with open("dummy.txt","w") as file:
#     file.write("Hello")

# os.chdir(r"E:\Sindhura\3RI\Python Repository\repository\Python1340")
# os.rmdir("dummy")


# try to remove the file and then remove the folder
os.chdir(r"E:\Sindhura\3RI\Python Repository\repository\Python1340\dummy")

os.remove("dummy.txt")

os.chdir(r"E:\Sindhura\3RI\Python Repository\repository\Python1340")
os.rmdir("dummy")

