


#scope of a varaiable...!
"""
it means the area of a program were a variable can be accesses or used
there are two type->local and global scope
local variable->Its variable declared inside a function ,
can be access only inside the function.
"""
# def show():
#     name="Reshma"
#     print(name)
# # print(name)
# show()

"""
Global variable->A variable decared inside the class and and its scope through out the class
"""
# name="reshma"
# def shows():
#     name="Arjun"
#     print(name)
# shows()
# print(name)

"""
using global keyworld we can modify the scope of a locally declared variable
"""

name="reshma"
x=200
print(name,x)
def shows():
    global name ,x
    name="Arjun"
    print(name)
    x=20
shows()
print(name,x)
