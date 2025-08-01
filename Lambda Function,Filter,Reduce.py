# Anyonymos functions/Headless functions
# Useful with filter functions,reduce functions,map functions etc..
def sq_num(n):
    return n**2
l2 = [34,56,78,12]
print("Using pre-defined function")
print(list(map(sq_num,l2)))
print("Using Lambda function")
#lambda n: n**2
print(list(map(lambda n: n**2,l2)))

even = lambda x:'even' if x%2==0 else 'odd'
print(even(34090))


'''syntax:
lambda agruments:expression
example: lambda x,y : x+y
'''

# usage with filter
# syntax: filter(function/predicate,iterable)
# l1 = [12,34,56,13,57,89]
# print(list(filter(lambda x:x%2==0,l1)))
# employee salary details. i want to extract salaries below 50000
print("==========================")
print("FILTER SCENARIO")
sal = [50000,45000,56000,35000,87000]
low_sal_data = list(filter(lambda x:x<50000,sal))
# sal[0] = 50000
# 50000<50000 =False: not to be considered
# sal[1] = 45000
#45000<50000 = True : to be considered
print(50000<50000)
print(low_sal_data)

#usage with reduce
# syntax: reduce(function,iterable)
# from functools import reduce
# print(reduce(lambda x,y:x+y,l1))
# concatenation of strings

from functools import reduce
raman_scores = (56,78,45,67,89)
print(f"Arithmetic output : {56+78+45+67+89}")
print(f"Output using sum function:{sum(raman_scores)}")

print("==================")
print("REDUCE scenario")
print(reduce(lambda x,y:x+y,raman_scores))
# (56,78,45,67,89)
# (56+78,45,67,89) = (134,45,67,89)
# (134+45,67,89) = (179,67,89)
# (179+67,89) = (246,89)
# (246,89) = 335

# product of entire data in list
print(reduce(lambda x,y:x*y,raman_scores))

# string concatenation
welcome_strng = ["Hello",".Welcome","to","the","session"]
print(reduce(lambda x,y:x+' '+y,welcome_strng))

# sorted function
# data = {"Raman":34,"Suman":78,"Baman":56,"Aman":90}
# print(sorted(data.items(),key=lambda x:x[0])) # key wise sorting
# print(sorted(data.items(),key=lambda x:x[1])) # value wise sorting

# emp_data = [(101,'raman'),(102,'thaman'),(103,'aman')]
# print(sorted(emp_data,key=lambda x:x[1]))
print("==========================")
print("Sorted function: ASCENDING ORDER")
student_scores = {"Raman":89,"Thaman":67,"Aman":56,"Baman":78,"Suman":98}
print(student_scores.items())
# sort it on basis of student names=> which are represented as keys  in student_scores dict
sorted(student_scores.items(),key=lambda x:x[0])
# sort it on basis of student marks => which are respresented as values in student_scores dict
sorted(student_scores.items(),key=lambda x:x[1])
# data = {"names":["raman","suman","thaman"]} doesnt work on such dictionaries
'''
SORTED FUNCTION BY DEFAULT SORTS IN ASCENDING ORDER
IF KEY IS NOT MENTIONED IN SORTED FUNCTION, IT SORTS ON BASIS OF 0TH POSITION 
I.E KEY OF DICTIONARY/1ST ELEMENT OF NESTED LIST
SORTED(DCT.ITEMS()) => THIS SORTS KEYS IN ASC ORDER
SORTED(DCT.ITEMS(),KEY=LAMBDA X:X[1]) => THIS SORTS VALUE IN ASC ORDER

TO SORT IN DESCENDING ORDER
SORTED(DCT.ITEMS(),REVERSE=TRUE)
'''
# if the sorted(key) : if lambda information is not passed, sorting happens for Index 0 position
print(sorted(student_scores.items()))

print("====================================")
print("DESCENDING ORDER")
# print(sorted(student_scores.items(),reverse=True))
print(sorted(student_scores.items(),reverse=True))
# sort the student marks in descending order
print(sorted(student_scores.items(),key=lambda x:x[1],reverse=True))

nested_data = [[101,"raman"],[102,"Baman"],[103,"Thaman"]]
nested_data = [[110,"Raman"],[123,"Baman"],[103,"Thaman"]]
print(sorted(nested_data,key=lambda x:x[1]))
print(sorted(nested_data)) # 0th position of nested list will be sorted in ascending order
print("DESCENDING ORDER-NESTED LIST")
print(sorted(nested_data,key=lambda x:x[1],reverse=True))
