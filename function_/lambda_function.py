"""
it's a small ananoumous function written mostly as a single expression using
lambda keyword.
Unlike a normal function created a fn def keyword, lambda fn does not required a fn name ot explicit return statement.

# syntax -> lambda parameters: expression.
# expresson operation is performed and automatically return as a results
"""
# write a fn for addition of 2 numbers.

# def sum(a,b):
#     return a+b
#
# sum_ = sum(10,20)
# print(sum_)

#using lambda function.
add = lambda a,b:a+b
print(add(10,20))

# write lambda function to find the square of the numbers
square = lambda a:a*a
print(square(5))

# check wheather the number is even or odd

result = lambda a:"even" if a%2==0 else "Odd"
print(result(30))

#non parametrized lambda function
greet = lambda :"Goog morning"
print(greet())

"""
String based questions:->
1. Write a prgrm check wheather gn char is a vowels or not(input->x="A")
2. Write a prgrm check wheather gn char is a consonent or vowels or not(input->x="A")
3. count the number of vowels in a user input.(input x="python")
4. count the number of vowels in a user input.(input x="python easy to learn")
Loop based question
1. Get the count of multiples of 5 from the gn list[x=[1,5,10,15,8,4]]
2. Identify the most repeat the element in the given list->[5,10,5,10,5,3,2]
3. Count the number of a string from the below list[5,10,"A","python","hello",3.5,False]



"""