# Decorators extend the functionality without making changes to the original functions
def mul(x:int,y:int):
    '''
    Input: Takes 2 integers as inputs
    Output: returns a product of provided inputs
    '''
    return x*y

#print(help(mul))

'''For example, in case of above multiply function,
If I want to make sure that whenever user uses multiply function, 
he should be able to use it only when he provides integer inputs. Else it should throw an error.
Install Ensure package using below command
pip install ensure
from ensure import ensure_annotations
'''
print(mul(50,2))
print(mul("A",3))
#print(mul('A','A'))
print(mul([1],2))
from ensure import ensure_annotations
@ensure_annotations
def mul2(x:int,y:int):
    '''
    Input: Takes 2 integers as inputs
    Output: returns a product of provided inputs
    '''
    return x*y

print(mul2(40,2))
#print(mul2("A",3))




'''
User defined decorator function syntax

def decorator_name(func):
    def wrapper(*args,**kwargs):
        before function execution
        result = func(*args,**kwargs)
        after function execution
        return result
    return wrapper
'''

# Scenario: Greeting Scenario
# Welcome user whenever he uses a function

def greeting(func):
    def wrapper(*args,**kwargs):
        print("Welcome to this page.")
        result = func(*args,**kwargs)
        print("Thank you for using this function")
        return result
    return wrapper

@greeting
def fact(n):
    b = 1
    for i in range(1,n+1):
        b = b*i
    return b

op = fact(10)
print(op)

print("=======================")
print("authentication scenario")
# Scenario: Authentication scenario
#Write a decorator which validates user details provided and allows only such users to access 
# the function who are present in its data.
data = {"Raman":"Ra23@12","Suman":"12@345s","Thaman":"456@34TH"}

def authenticate(func):
    def wrapper(username,password,*args,**kwargs):
        if username in data.keys() and (password == data.get(username)):
            print("Authentication is successful")
            result = func(username,password,*args,**kwargs)
            return result
        else:
            print("Authentication is unsucessful")
    return wrapper

@authenticate
def user_details(username,password,account_number):
    print(f"DETAILS ARE: {account_number}")

user_details("Raman","Ra23@12",3434324234)
print("========================")
user_details("Raman","Ra2",3434324234)
