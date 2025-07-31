import random
# Iterators can be used on Sequential datatypes/ collection data
greeting = "Welcome to the session"
emp_data = [101,"Raman",345345345]
emp_ids = (101,102,103,104)
emp_details = {"ids":[12,13,14,15,16],"names":["Raman","Thaman","Suman"]}
emp_set = {201,202,203,204}

it1 = iter(greeting)
print(next(it1))
print(next(it1))
it2 = iter(emp_data)
print("=================")
print("List Iterator")
for _ in range(len(emp_data)):
    print(next(it2))
print("=================")
print("Tuple Iterator")
it3 = iter(emp_ids)
for _ in range(len(emp_ids)):
    print(next(it3))
print("=================")
print("Dictionary Iterator")
it4 = iter(emp_details)
for _ in range(len(emp_details)):
    print(next(it4))

# Custom Iterators
print("==============================")
print("Customised Iterator that displays Top Ten numbers")
class TopTen:
    def __init__(self):
        self.num = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.num<=10:
            val = self.num
            self.num = self.num+1
            return val
        else:
            raise StopIteration

ten1 = TopTen()
for _ in range(10):
    print(next(ten1))

# Custom Iterators
print("==============================")
print("Customised Iterator that generates random numbers when a Dice is thrown")
class Dice:
    def __iter__(self):
        return self
    def __next__(self):
        c = random.randint(1,6)
        return c
d1 = Dice()
print(next(d1))
for _ in range(10):
    print(next(d1))

print("==========================")
print("Create a custom Iterator that generates Even numbers")
class EvenNumbers:
    def __iter__(self):
        self.num = 2
        return self
    def __next__(self):
        x = self.num
        self.num = self.num + 2
        return x

even_50 = EvenNumbers()
it_even = iter(even_50)
print(next(it_even))
for _ in range(50):
    print(next(it_even))