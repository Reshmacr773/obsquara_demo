#21/10/2026
#mutable datatype-list, set, dictionary
#immutable datatype int,flat,tuple, boolean.

import keyword
#string methods-
name = "Reshma"
print(keyword.kwlist)

#keywords-meaningful words in python cannot be provideds a variable name
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break',
# 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for',
# 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or',
# 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
# difference between keyword, identifier and variable

"""
variable declaration can be perform to store or assigned values
variable declaration examples
"""
x = 10
X = 20
abc = 12
ABC = 23
abc_= 45
_abc= 87
ab_c = 12
_=50
abc123 = 67
a12_c = 123
#12abc = 7   variables cannot start with a digits, spaces are not allowed
#must start with letter or special character special characters not allows
"""
identifiers are variable which are meaningful in nature
"""

name = "prabha"
age = 23
price = 20.9

#case-sensitivity in python.
"""
unicode represents a characters indiviual codes repsrentation in normal english. 
"""

xyz = "Reshma"
XYZ = "Shyama"
print(XYZ)

a="Python"
b="python"
print(a==b) #check both case and value and return a boolean response

#string methods
"""str1="ReshmaABC is a student"
print(str1.upper())
x= str1.lower()

print(str1.capitalize())#first letter of first word get uppercase
print(str1.title()) # first letter of all keys get upper key
print(str1.swapcase())  
print(str1.find("is"))
print(str1.index("is"))
print(str1.count("a"))
print(str1.isupper())
print(str1.islower())
print(str1.isdigit())
print(str1.isdigit())
print(f"The original string is: {str1}")"""

#list method
list1 = [1,2,3, 10, "Varsha"]
list1.append("Geethu") # To add new element into  the existing list. its add only into last element.
print(list1)
list1.pop() # To delete elemet from last index
print(list1)



#22/10/2026
list2 = [10,20,30,40, "paaru"]
list1.extend(list2)
print(list1)

list1.insert(0,"Gpay")
print(list1)
list1.remove("Varsha")  #remove only first occurance of the element.                u8u                  -*
print(list1)
print(list1.count(10))
# list1.clear() #to clear the data from list but list only remians there
# print(list1)

list1.reverse()
print(list1)

list3=list1.copy()
print(list3)

list4 = [2.5,0,-10, 100, 0.5]
list4.sort() #to convert acending oder
print(list4)

list4.sort(reverse=True) #to convert descending oder
print(list4)

list5 = ["book", "pen", "p", "APPLE", "PEN"]
list5.sort() #converts in alph
print(list5)

"""
methods-> appends,pop, insert,clear, extend,sort, copy, remove
"""

#build in methods in python list

num = [2,1,100,2.5]
print(len(num))
print(min(num))
print(max(num))
print(sum(num))


"""
intreview questions:->

"""

list_new = [10,20,30,40]
new="ABC"

#expected output [10,20,"ABC", 30,40]

list_new.insert(2,new)
print(list_new)

#tuple methods

num=(2,3,4,10,3,3)
print(num.count(3))
print(num.index(3))

#create a tuple and add new elements in its second last index postion.
print(type(num))
num=list(num)
print(type(num))
num.insert(-2, "newly added")
num=tuple(num)
print(num)

#packing and unpacking of tuple.
student=("minnu", 37, "Female","Ernakulam","kollam")
name,age,gender,*place =student
print(name,age,gender)
print(place)

alphabets=("a","b","C","d","E","f")
x,*y,z=alphabets
print(x,z)
print(y)

#dictionary methods
dict={"name":"Reshma","age":30,"gender":"F"}
print(dict["name"]) #for getting value against the key
dict["loaction"]="TVM"
print(dict)
print(dict.get("age")) #to get the value
dict.update({"age":31})
print(dict)
dict["name"]="Aparna"#this method working-checking key is there if not add into last otherwise it will update the already existing value
print(dict)
print(dict.keys())
print(dict.values())
print(dict.items())#in single dictionary each key-value pair called as items
