"""
Its program approach, in which we aorganize our code using classes and object.
Real world example:->
A car category has a properties(brand,colour,model,speed etc) and behaviours(start,stop,accelerate,break)
Each car object under the category has its own property.
In real use programmin properties are repesents using attributes.
Behaviours are using methods(function using inside the class)
Objects are instants of a cass
class is blueprint of object
Terms in OOPS->Class, object,attributes,methods
Advantages:->
1.Code re-usability
2.Maintainability
3.Encapsulating data and its objects
4.Organising entire code scripts
5 Secuirity,quality assurance
"""
class CarClass:
    color='black'
    model="electric"

    def start(self): # self refers currents object using with we involk the method
        print("Engine started")

    def stop(self,distance):
        self.distance = distance #imstance object created to used to usied to others methods inside the classes
        print(f"Car stopped at {distance}")


    def detail(self):
        print(f"Car started and stoped at {self.distance} kilometers") #

car1=CarClass() #creating objects
# print(color) cannot be access, access only inside the class, if need to access by using class objects
print(car1.color)
car2=CarClass()
print(car2.model)
car1.speed="100kmph"
print(car1.speed)
# print(car2.speed) Cannot be access speed, its the propeties of object car1
car1.start()
car2.start()
# car2.stop(10)
car1.stop(20)
car1.detail()


