# Length function
st1 = "Welcome to the session"
lst1 = [34,56,78,90]
empids = (101,102,103,104)

print(f"Length of the string: {len(st1)}")
print(f"Length of the string: {len(lst1)}")
print(f"Length of the string: {len(empids)}")

# create a user defined polymorphism scenario
class India:
    def __init__(self):
        pass
    def capital(self):
        print("Capital of India is Delhi")

class UnitedStates:
    def __init__(self):
        pass
    def capital(self):
        print("Capital of US is Washington")

india1 = India()
india1.capital()
print("---------------------")
us1 = UnitedStates()
us1.capital()

print("------------------")
print("You can also create a function which takes object as input")
def capital_country(country_object):
    country_object.capital()

capital_country(India())
capital_country(UnitedStates())
print("-----------------")
# you can also pass data in below way.
i1 = India()
capital_country(i1)

# Operator Overriding
print("----------------------")
print("Operator Overriding")
c1 = 56 + 78
c2 = "Raman" + " " + "Patil"
c3 = [3,4] + [4,5]
print(f"Addition of two numbers: {c1}")
print(f"Combined string is : {c2}")
print(f"Combined lists are : {c3}")

c4 = 56*78
c5 = "Raman" * 3
# c7 = "raman" * "K" # this will throw an error which is as per the functionality
c6 = [5,6] * 4

print(f"Multiplication of two numbers: {c4}")
print(f"New string is : {c5}")
print(f"New data in list is : {c6}")



