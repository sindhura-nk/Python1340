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

# To access the methods of class Person
c1.welcome()
c1.work()
c2.welcome()
c2.work()

# you can create methods with specific parameters as well. When the object calls the method, we need to pass that paramter data also
class Person2:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def welcome(self):
        print(f"Welcome to the session {self.name}. Hope you find it insightful.")
    
    def work(self,company):
        self.company = company
        print(f"{self.name} works at {self.company}")

print("-------------------")
print("Person2 class output: ")
cp1 = Person2("Thaman",65)
cp1.work("3RI")
        
# you can create a class where init doesnt take any parameters. you can define methods which take respective parameters
class Person3:
    def __init__(self):
        print("Intialized")
    
    def welcome(self,name):
        self.name = name
        print(f"Welcome {self.name}")

print("-------------------")
print("Person3 class output ")
cp2 = Person3()
cp2.welcome("Naman")
# you can also create methods that dont use instance attributes(i.e without using self). use @staticmethod decorator
class Person4:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    @staticmethod
    def greeting():
        print("Welcome to this session. I hope you are enjoying it")

print("-------------------")
print("Person4 class output ")

cp3 = Person4("Baman",45)
cp3.greeting()

# class attributes
'''
class class_name:
    # class attributes
    parameter1 = "abc"
    parameter2 = "xyz

    # to use the class attributes in methods, u can use @classmethod decorator
    @classmethod
    def method1(cls): # pass cls as the input parameter
        pass # to access class attributes, use cls.parameter1 or cls.parameter2
'''
class Person5:
    # class attributes
    Institute = "3RI"
    Course = "Python"

    def __init__(self):
        print("Intialized")
    
    def welcome(self,name):
        self.name = name
        print(f"Welcome {self.name}")
    
    @classmethod
    def course_data(cls):
        print(f"welcome to {cls.Institute}. You have enrolled for {cls.Course}")

print("-----------------")
print("Person5 class output")
cp4 = Person5()
cp4.course_data()
cp4.Institute
cp4.Course

cp5 = Person5()
cp5.course_data()
cp5.Institute
cp5.Course


'''
Scenario1: 
Create a class blank account with attributes as account holder name,balance,account number.
Define below methods: 
withdrawal
deposit
transfer
'''
class bank_account:
    # class attributes
    bank_name = "HDFC"
    branch = "Pimple Saudagar"

    # instance attributes
    def __init__(self,account_holder_name,balance,account_number):
        self.account_holder_name = account_holder_name
        self.balance = balance
        self.account_number = account_number
        self.url = "https://en.wikipedia.org/wiki/Data_analysis"
    
    @classmethod
    def welcome(cls):
        print(f"Welcome to {cls.bank_name} at {cls.branch}. We are happy to assist you")
    
    def withdrawal(self,amount):
        self.amount = amount
        if self.amount < self.balance:
            self.balance = self.balance - self.amount
            print(f"Withdrawal of amount {self.amount} successful. Your new balance is {self.balance}")
        else:
            print(f"Insufficient balance. Cannot proceed with withdrawal")
    
    def deposit(self,amount1):
        self.amount1 = amount1
        self.balance = self.balance + self.amount1
        print(f"Deposit successful. Your new balance is {self.balance}")
    
    def transfer(self,amount2):
        self.amount2 = amount2
        if self.amount2 < self.balance:
            self.balance = self.balance - self.amount2
            print(f"Transfer of amount {self.amount2} successful. Your new balance is {self.balance}")
        else:
            print(f"Insufficient balance. Cannot proceed with Transfer")

print("============================")
print("Scenario1 output")
user1 = bank_account("Suman",80000,2345678967)
print(f"{user1.account_holder_name} details: ")
user1.deposit(15000)
user1.transfer(10000)

user2 = bank_account("Thaman",45000,8987676756)
print(f"{user2.account_holder_name} details: ")
user2.withdrawal(50000)


    
