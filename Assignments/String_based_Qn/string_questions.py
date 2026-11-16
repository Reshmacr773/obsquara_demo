"""
Questions:->
String based questions:->
1. Write a prgrm check wheather gn char is a vowels or not(input->x="A")
2. Write a prgrm check wheather gn char is a consonent or vowels or not(input->x="A")
3. count the number of vowels in a user input.(input x="python")
4. count the number of vowels in a user input.(input x="python easy to learn")
"""

#1
vowels = 'AIOUEaioue'
x='A'
if x in vowels:
    print(f'{x} is in vowels')
else:
    print(f"{x} is not in vowels")
#2
if x in vowels:
    print(f'{x} is in vowels')
else:
    print(f'{x} is in Consonent')



#3
x="python"
count=0
for items in x:
    if items in vowels:
        count+=1
    else:
        continue
print(f'{count}')

#4
x="python easy to learn"
vowels_count = 0
for items in x:
    if items in vowels:
        vowels_count+=1
    else:
        continue
print(vowels_count)




