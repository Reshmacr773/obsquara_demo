org_string = "reshma is good girl and she is 30 years old.also she is a mother of Yaamibaby"
"""
*********string methods*****************
print(org_string.index("is"))
print(org_string.count("is"))
print(len(org_string))
print(org_string.capitalize())
print(org_string.title())
print(org_string.swapcase())
print(org_string.find("is"))
upper_string = org_string.upper()
print(upper_string.isupper())
lower_string = org_string.lower()
print(lower_string.islower())
"""

orginal_list = [10,20.7,29,"Reshma",True]
list1 = [1,2,3, 10, "Varsha"]
# orginal_list.extend(list1)
# print(orginal_list)
orginal_list.append("Charutha")
print(orginal_list)
# orginal_list.clear()
orginal_list.remove("Charutha")
print(orginal_list)
orginal_list.pop()
print(orginal_list)

orginal_list.insert(3,"Apple")
print(orginal_list)

copy_value= orginal_list.copy()
copy_value.insert(4,"From Ernakulam")
print(copy_value)