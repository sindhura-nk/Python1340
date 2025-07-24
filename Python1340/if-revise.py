lst = [34,56,78,90,33,99,87]
for i in lst:
    if i%2==0:
        print(f"{i} is even number")
    else:
        print(f"{i} is an odd number")

def check_even_odd(l1):
    for i in l1:
        if i%2==0:
            return f"{i} is Even"
        else:
            return f"{i} is Odd"
print(check_even_odd(lst))

def check_even_odd_oneparameter(a):
    if a%2==0:
        return f"{a} is Even"
    else:
        return f"{a} is Odd"

for i in lst:
    print(check_even_odd_oneparameter(i))
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
'''
