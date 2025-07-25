# write()
with open("sample.txt","w") as file:
    file.write("What if we want to store the data that were input as well as the generated output permanently so that we can reuse it later?\n.Usually, organizations would want to permanently store information about employees, inventory, sales, etc. to avoid repetitive tasks of entering the same data.\n Hence, data are stored permanently on secondary storage devices for reusability.")

with open("sample.txt","r") as file:
    print(file.read())

# writelines() : u can pass the data in a list format. you must provide \n whenever u want the data in new lines
list_data = ["Raman","Thaman","Suman","Baman"]
with open("sample.txt","w") as file:
    file.writelines(list_data)

with open("sample.txt","r") as file:
    print(file.read())

list_data2 = ["\nRaman\n","Thaman\n","Suman\n","Baman\n"]
with open("sample.txt","a+") as file:
    file.writelines(list_data2)
    print(file.read())

with open("sample.txt","r") as file:
    print(file.read())