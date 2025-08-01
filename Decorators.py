# Decorators extend the functionality without making changes to the original functions
def mul(x:int,y:int):
    return x*y

print(help(mul))

'''For example, in case of above multiply function,
If I want to make sure that whenever user uses multiply function, 
he should be able to use it only when he provides integer inputs. Else it should throw an error.
Install Ensure package using below command
pip install ensure
from ensure import ensure_annotations
'''




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

# Scenario: Authentication scenario
#Write a decorator which validates user details provided and allows only such users to access 
# the function who are present in its data.
