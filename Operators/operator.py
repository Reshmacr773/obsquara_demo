#Arithmatics operators-> +,-,*,%,/,//,**
"""
a,b = 10,20
print(a+b) #30
print(a-b) #-10
print(a*b) #200
print(a/b) #0.5 (normal division)
print(a//b) #0 (floor division)
print(a%b)  #  (remainder/modular division)
print(a**2) # (syntax-> base**exponent)

a,b = "Hello ", "Reshma"
print(a+b) #concatination

a, b = 10, "hello"
print(a+b)"""

#comparison operators - >, <, <=, >=, =, ==, != (returns a boolean value)
a, b = 20, "20"
# print(a>b)
print(a==b) # check both tha value and datype equal or not.
print(a!=b)

#assignment operators

a,b = 10,20
a= a+b
print(a) #30

a,b = 10,20
a+=b #a-=b,a*=b etc possible for the all arithmetic operators
print(a) #30

#logical operators ->and,or,not

a,b,c = 10,20,30
print(a<b and b>c and c>a) #returns true if all conditions are True
print(a<b or b>c or c>a) #if anyone of the condition is true returns True
print(not b>c)

#membership operators -> in, not in

a="Hello"
print("O" in a)

b = [10, 20, 30, 40]
print(50 not in b)

#identity operators -> is, is not (equal as ==, !=)
a,b = 10,20
print(a is b)

