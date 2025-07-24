# simple datatypes
name = "Raman"
mobile = 456456565
temp = 98.7
married = True
# complex datatypes
empdata = [34,56,'raman']
empdata_2 = (45,67,'thaman')
empids = {101,102,103,103}

emp_data = {'ids':[101,102,103],'names':['raman','thaman','suman']}
emp_2 = set()

# lst= [12,34,56,67]
# write a program that calculates squares of elements in lst and return a new list
lst= [12,34,56,67]
new_lst = []
for i in lst:
    c = i**2
    new_lst.append(c)
print(new_lst)

# create a function for above task-assume I have repeated use of that code
def sq_nums(l1):
    new_lst = []
    for i in l1:
        c = i**2
        new_lst.append(c)
    return new_lst

sq_lst = sq_nums(lst)
print(f"This output is from function sq_nums: {sq_lst}")

lst2 = input("Please enter data separated by space").split()
new_lst2 = []
for i in lst2:
    #new_lst2.append(int(i))
    c = int(i)
    new_lst2.append(c)
print("Output of input function is ",new_lst2)
print(f"Output of input function is {new_lst2}")
sq_lst2 = sq_nums(new_lst2)
print(f"Output of sq_nums function for input data: {sq_lst2}")


def sq_nums_input():
    lst3 = input("Please enter a number separated by space ").split()
    new_lst3 = []
    for i in lst3:
        c = int(i)
        d = c**2
        new_lst3.append(d)
    return new_lst3

sq_lst3 = sq_nums_input()
print(f"Output of sq_nums_input function which takes input data: {sq_lst3}")






