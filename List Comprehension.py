updated_sal = []
sal = [35000,45000,67000,78000]
pf = 800
for i in sal:
    #updated_sal.append(i-pf)
    c = (i-pf)
    updated_sal.append(c)
print(updated_sal)

print("Using list comprehension")
# list comprehension
# new_list_name = [value_to_be_appended for i in iterable]
updated_sal2 = [(i-pf) for i in sal]
print(updated_sal2)

print("====================")
print("List comprehension for one IF condition")
# check if number is even
all_data = [890,98,99,77,56,44,33]
# 890,98,56,44
even_list = [i for i in all_data if i%2==0]
print(even_list)

print("List comprehension using IF ELSE condition")

# check if a number is positive or negative
data = [90,-89,78,56,-67,-34,78,56]
data_pos_neg = []
for i in data:
    if i<0:
        data_pos_neg.append("Negative")
    else:
        data_pos_neg.append("Positive")
print(data_pos_neg)

data_list_comp = ["Negative" if i<0 else "Positive" for i in data]
print(f"Using list comprehensio: {data_list_comp}")


