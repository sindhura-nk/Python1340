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





# Hierarchal Inheritance