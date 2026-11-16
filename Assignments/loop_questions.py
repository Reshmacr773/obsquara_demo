"""
Loop based question
1. Get the count of multiples of 5 from the gn list[x=[1,5,10,15,8,4]]
2. Identify the most repeat the element in the given list->[5,10,5,10,5,3,2]
3. Count the number of a string from the below list[5,10,"A","python","hello",3.5,False]
"""

#1
x=[1,5,10,15,8,4]
mul_count = 0
for list_item in x:
    if list_item%5==0:
        mul_count+=1
    else:
        continue
print(mul_count)

#2
my_list = [5, 10, 5, 10, 5, 3, 2]
most_repeated = max(my_list, key=my_list.count)
print(most_repeated)

# x_ = [5,10,5,10,5,3,2]
# least_count_list = []
# count=0
# for item_ in x_:
#     for y in x_:
#         if item_ == y:
#             count+=1
#         else:
#             continue
#     least_count_list.append(count)
# print(least_count_list)

#3

find_string_ = [5,10,"A","python","hello",3.5,False]
str_count=0
for items in find_string_:
       if type(items) is str:
           str_count+=1
print(str_count)



