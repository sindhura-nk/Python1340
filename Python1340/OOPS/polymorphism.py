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



