'''
syntax:
class class_name:
    # Initialize all the varibles 
    def __init__(self,parameters1,parameters2):
        self.parameters1 = parameters1
        self.paramters2 = parameters2
    
    def method1(self):
        pass

    def method2(self):
        pass
'''  

class Person:
    # Initialize all the varibles 
    def __init__(self,name,age):
        self.name = name
        self.age = age
        #c1.name = "raman"
        #c1.age = 45
        #c2.name = "suman"
        #c2.age = 67
    
    def welcome(self):
        print(f"Welcome to the session {self.name}. Hope you find it insightful.")
    
    def work(self):
        print(f"We currently have openings for Data Analyst. If you are 18 and above you can apply")
        if self.age > 18:
            print("Apply for the job using below link.")
        else:
            print("Sorry you are not eligible.")


# define class objects
c1 = Person("raman",45)
c2 = Person("suman",17)
# retrieve the attributes of c1 object
print(c1.name)
print(c1.age)
# retrieve the attributes of c2 object
print(c2.name)
print(c2.age)

# create an object and always pass all the parameters. If we wont pass all, we will get an error
#c3 =  Person("Chaman")

c1.welcome()
c1.work()
c2.welcome()
c2.work()
