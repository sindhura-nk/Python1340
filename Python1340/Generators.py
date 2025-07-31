## Generator Functions
# Range function
print(range(10,20))
data1 = list(range(10,20))
data2 = tuple(range(10,20))
print(data1,'\t',data2)
for i in range(10,20):
    print(i)

# Enumerate function : Provides numbering to each element of a list/tuple.
print(enumerate(data1))
print(list(enumerate(data1)))
for i,j in enumerate(data1):
    print(f"Enumerate numbering: {i}")
    print(f"Value of List: {j}")
# changing the default numbering 
for i,j in enumerate(data1,250):
    print(f"Enumerate numbering starting from 250: {i}")
    print(f"Value of List: {j}")

# use case
search = 19
for i,j in enumerate(data1):
    if j == search:
        print(f"Found the {search} value at index position {i}")
    else:
        print(f"{search} is not present in the list")

# Zip function: Combines the elements present in both lists at index level.
print("======================")
print("zip function")
country = ["India","Russia","Australia"]
codes = ["IN","RU","AU"]
print(zip(country,codes))
country_with_codes = list(zip(country,codes))
print(country_with_codes)
codes_of_countries = tuple(zip(codes,country))
print(codes_of_countries)
print("===============")
print("Zip function used on varying lengths of lists")
fruits = ["apple","banana","cherry"]
calories = [15,25,10,15,45]
print(list(zip(fruits,calories)))

# Map function
student_scores = input("Enter your scores provided by space").split()
print(student_scores)
student_new = []
for i in student_scores:
    c = int(i)
    student_new.append(c)
print(student_new)
print("=========================")
print("above scenario using map function")
print(list(map(int,student_scores)))

print(list(map(int,input("Enter scores separated by space").split())))

## 
def sq_nums(num):
    c = num**2
    return c

op1 = sq_nums(90)
print(op1)
op2 = sq_nums(89.90)
print(op2)
# op3 = sq_nums([45,67,89])
# print(op3)
lst = [45,67,89]
c = []
for i in lst:
    p = sq_nums(i)
    c.append(p)
print(c)
# above output using map function
print("================")
print("above output using map function")
print(list(map(sq_nums,lst)))

# Customised Generator function/User Defined Generator function
'''
def function_name:
    logic
    yield value
'''
print("=======================")
print("User defined Generator function")
def fibonacci(n):
    a,b = 0,1
    for _ in range(n):
        yield a
        a,b = b,a+b
print(list(fibonacci(50)))

# def fibonacci_2(n):
#     a = 0
#     b = 1
#     for _ in range(n):
#         yield a
#         a = b
#         b = a+b
# print(list(fibonacci_2(50)))

def arthm_operations(x,y):
    return x+y

print("---------------")
print("Multiple yeild can be used")
def arthm_operations_2(x,y):
    yield x*y
    yield x+y
    yield x-y
    yield x/y

for i in arthm_operations_2(90,50):
    print(i)