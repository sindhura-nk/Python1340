lst = [45,56,67,89,90,125]

# index position wise looping the list
for i in range(len(lst)):
    print(i,lst[i])

# run a loop through each element of the list
print("===================")
for i in lst:
    print(i)

# dictionary containing data
emp_data = {"suman":90,"thaman":89,"baman":67,"raman":34}

print("====================")
# run a loop through dictionary to access keys
for key in emp_data:
    print(key)
print("=========")
for key in emp_data.keys():
    print(key)
# run a loop through dictionary to access keys
print("==================")
for value in emp_data.values():
    print(value)
print("=================")
# run a loop through dictionary to access both key and values
for key,value in emp_data.items():
    print(key,"=>",value)
print("===================")
for i in range(1,11):
    print("Welcome to the session")
print("============")
for i,j in enumerate(lst):
    print(i,j)

print("=========================")
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def scores(self,score):
        self.score = score
        print(f"Scores of student {self.name} are {self.score}")

s1 = Student("raman",15)
s2 = Student("thaman",14)
print(s1.age)
print(s1.name)
print(s2.name)
s1.scores(67)
s2.scores(89)
print("======================")
print("====================")
# strings
st1 = "   Welcome to the session   "
print(st1.split())
print(st1)
print(st1.strip(" "))
print(st1)
st1 = st1.strip()
print(st1)
st1.replace(st1,"Session completed today. thankyou for the inputs")
print("===================")

print("FILE HANDLING")
# file handling
with open("sample.txt","r") as file:
    r1 = file.read()
    print(r1)

with open("sample.txt","w") as file:
    file.write("This is replacing my existing content")

with open("sample.txt","a") as file:
    file.write(" Adding new content to my existing file")

print("Image file")

with open("Python1340/ffhq_1982.png","rb") as file:
    print(file.read())

print("===============")
# functions
def school_data():
    school_name = "SNBP"
    school_branch = "Pimple Saudagar"
    return f"School information: {school_name}, {school_branch}"

def student_data(name,scores):
    if scores>60:
        print(f"Student with {name} has passed with distinction scoring {scores}.")
    else:
        print(f"Student with {name} has failed and expected to re-take the examination.")

sd1 = student_data("Raman",56)
#sd2 = student_data("Raman")
print("==========================")
# variadic functions
data = ["raman","suman","thaman","baman"]
def student_name(*args):
    for i in args:
        if i in data:
            print(f"Sharing details of student {i}")
        else:
            print(f"Student data is not available")

student_name("raman")
student_name("raman","aman")
print("========================")
def student_data2(**kwargs):
    for name,score in kwargs.items():
        if score>60:
            print(f"Student with {name} has passed with distinction scoring {score}.")
        else:
            print(f"Student with {name} has failed and expected to re-take the examination.")
student_data2(Raman=56,Thaman=34)
student_data2(Suman=89,Baman=34,Nama=95)


            
