# Single Level Inheritance
class Student:
    def __init__(self,name,roll_no):
        self.name = name
        self.roll_no = roll_no
    
    def student_joining(self):
        print(f"This student {self.name} has joined us on 23-02-2018")

# class Scores(Student):
#     def __init__(self,math_score,science_score):
#         self.math_score = math_score
#         self.science_score = science_score
# the above code will give you an error as we have not established the link between 2 classes

class Scores(Student):
    def __init__(self, name, roll_no,math_score,science_score):
        super().__init__(name, roll_no)
        #Student.__init__(name,roll_no)
        self.math_score = math_score
        self.science_score = science_score
    
    def display_scores(self):
        super().student_joining()
        #Student.student_joining()
        print(f"Math Scores of student are: {self.math_score}")
        print(f"Science scores of student are: {self.science_score}")

S1 = Student("Raman",13)
#Sc1 = Scores(56,89)
Sc2 = Scores("Raman",13,89,90)
Sc2.display_scores()
print(Sc2.math_score)
print(Sc2.science_score)
print(Sc2.name)
print(Sc2.roll_no)

class Animal:
    def __init__(self,animal_name):
        self.animal_name = animal_name
    def animal_sound(self):
        print(f"Animal Sound is heard")
    def animal_qualities(self):
        print(f"Animals have 4 legs")
    
class Dog(Animal):
    def __init__(self, animal_name,breed):
        super().__init__(animal_name)
        self.breed = breed
    def animal_sound(self):
        super().animal_sound()
        super().animal_qualities()
        print(f"Dog barks")

print("--------------------")
print("Child class object output")
d1 = Dog("DOG","Labrador")
d1.animal_sound()

print("--------------------")
print("Parent class object output")
animal1 = Animal("Cat")
animal1.animal_sound()

# Multi level Inheritance
print("=============================================")
print("MULTI LEVEL INHERITANCE")
class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def Employee_Data(self):
        print(f"Employee ID of {self.name} is {self.id}")

class Manager(Employee):
    def __init__(self, name, id,team_name):
        super().__init__(name, id)
        self.team_name = team_name
    def Manager_Info(self):
        #super().Employee_Data()
        print(f"This employee works in {self.team_name}")

class Project_Manager(Manager):
    def __init__(self, name, id, team_name,project_name):
        super().__init__(name, id, team_name)
        self.project_name = project_name
    def Project_Data(self):
        super().Employee_Data()
        super().Manager_Info()
        print(f"This Employee now got promoted and works in {self.project_name}")

# Employee object
print("Employee object Output: ")
e1= Employee("Raman",102)
e1.Employee_Data()

print("Manager Object Output: ")
m1 = Manager("Suman",145,"E2K")
m1.Manager_Info()

print("Project Manager Output")
p1 = Project_Manager("Thaman",190,"C3K","UPS")
p1.Project_Data()
p1.Employee_Data()
p1.Manager_Info()


# Hierarchal Inheritance
print("============================")
print("Hierarchal Output")
class Showroom:
    def __init__(self,showroom_name,branch):
        self.showroom_name = showroom_name
        self.branch = branch
    def greeting(self):
        print(f"Welcome to our showroom {self.showroom_name} located at {self.branch}")
class Model1(Showroom):
    def __init__(self, showroom_name, branch,price_range):
        super().__init__(showroom_name, branch)
        self.price_range = price_range
    def Model1_Details(self):
        super().greeting()
        # price_range = int(input("Please enter your price range in a single number format. Ex:12"))
        # when you are using input(), in this scenario donot use price_range as instance attribute
        if 10 < self.price_range <15:
            print(f"Details of the car are : Grand i10. Colors available is Red")
        elif 0 < self.price_range >15:
            print(f"For this range, we are providing a high end model-Grand i20. Kindly let us know if you are interested")
        else:
            print("Sorry. Our car range starts from 10.5L")
class Model2(Showroom):
    def __init__(self, showroom_name, branch,price_range):
        super().__init__(showroom_name, branch)
        self.price_range = price_range
    def Model2_Details(self):
        if self.price_range >15:
            print(f"Details of the car are : Grand i20. Colors available is Red")
        elif 10< self.price_range <15:
            print(f"For this range, we are providing a high end model-Grand i10. Kindly let us know if you are interested")
        else:
            print("Sorry. Our car range starts from 10.5L")

print("Model1 output")
m1_1 = Model1("Garve Hyundai","Wakad",20) 
m1_1.Model1_Details()
print("Model2 Output")
m2_1 = Model2("Garve Hyundai","Ravet",19)
m2_1.Model2_Details()
        