"""
Constructor is special method and its automatically called or involked when an object is created.
Purpose:->Initialize object attributes, assign initial value to variable, perform initial set up.
"""
class Parent:
    def __init__(self,name,age):
        print("Constructor created! ")
        self.name= name
        self.age= age

    def display(self):
        print("Parent method! ")
        print(self.name,self.age)

obj = Parent("Reshma",30)
obj.display()

obj2 = Parent("Yaami", 2)
obj2.display()

#Destructor!
"""
Its a special method python may call when an object about to be distroy.
purpose:perform clean up opearations, close files or connection.
"""