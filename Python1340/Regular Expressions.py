# Regular Expressions are used to find a pattern/string/set of strings.
st1 = "Welcome to the session. Session starts at 9:30 AM."
# Search for session in above string

if "session12" in st1.lower():
    print("It is present")
else:
    print("It is not present")

# Search for session in above string. It must start with capitals followed by small letters and numbers
import re
p = "session"
match1 = re.findall(p,st1)
print(match1)
p1 = r"[abc]"
# \n \t \s
match2 = re.findall(p1,st1)
print(match2)
p2 = r"[a-z]"
match3 = re.findall(p2,st1)
print(match3)
p3 = r"\d"
p3 = r"[0-9]"
match4 = re.findall(p3,st1)
print(match4)
p4 = r"\d+"
match5 = re.findall(p4,st1)
print(match5)
p5 = r"[A-Z][a-z][0-9]" # capital character followed by small followed by digits
match6 = re.findall(p5,st1)
print(match6)
p6 = r"[A-Z a-z 0-9]"
match7 = re.findall(p6,st1)
print(match7)
p5 = r"[A-Z][a-z][0-9]"
match8 = re.findall(p5,st1)
print(match8)
p6 = r"[A-Z][a-z]+"
print(st1)
match9 = re.findall(p6,st1)
print(match9)
st2 = "Welcome to the Session. Session starts at 9:30 AM."
p7 = r"[A-Z][a-z]+"
match10 = re.findall(p7,st2)
print(match10)

print("===========================")
print("split()")
# split()
pattern1 = r"\d"
d1 = re.split(pattern1,st2)
print(d1)
pattern2 = r"\."
d2 = re.split(pattern2,st2)
print(d2)

print("==================")
print("Search and NOT")
# search()
# search for data that are not numbers
pattern3 = r"[^0-9]"
match = re.findall(pattern3,st2)
print(match)
m1 = re.search(pattern3,st2)
if m1:
    print("This pattern is identified ")
else:
    print("Not identified")

mobile_pattern = r"[6 7 8 9][0-9]{9}"
user_ip = int(input("Please enter your phone number"))
m2 = re.search(mobile_pattern,user_ip)
if m2:
    print("Mobile number is correctly entered.")
else:
    print("Mobile number is incorrect.")
print("===================")
print("substitute")
# sub()
user_review = "Wow... Loved this place."
pat1 = r"[^a-z A-Z]"
user_updated = re.sub(pat1,"",user_review)
print(user_review)
print(user_updated)

# substitute numbers with **
conf_data = "Hello, User with account number 87879870 has registered today"
pat2 = r"[^a-zA-Z]"
pat3 = r"\d+"
# pat4 = r"\d"
new_data = re.sub(pat2,"*",conf_data)
print(new_data)
new_daat2 = re.sub(pat3,"*",conf_data)
print(new_daat2)