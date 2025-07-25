'''
 Assignment : Dictionary should contain student name and marks
Write a function which takes dictionary as input, and provide corresponding grades to the students based on their marks
student_marks = {"Raman":90,"Thaman":34,"Suman":56,"Baman":78}
Grades:
80-90 : A
70-80: B
60-70:C
50-60:D
40-50: E
<40: F
Output:
student_grades = {"Raman":"A","Thaman":"F","Suman":"D","Baman":"B"}
'''
student_marks = {"Raman":90,"Thaman":34,"Suman":56,"Baman":78}
def grades(marks):
    if 80<=marks<=90:
        return 'A'
    elif 70<=marks<80:
        return 'B'
    elif 60<=marks<70:
        return 'C'
    elif 50<=marks<60:
        return 'D'
    elif 40<=marks<50:
        return 'E'
    elif marks<40:
        return 'F'
    else:
        return 'Invalid Input'

def student_grades(data):
    mark_grade = {}
    for name,mark in data.items():
        mark_grade[name] = grades(mark)
    return mark_grade

op_grades = student_grades(student_marks)
print(op_grades)
