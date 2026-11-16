#write python prgm to check wheather the number is prime
#prime numbers 2,3,5,7,11,13,17...-its divisible by one and itself
#consider 7(find the remainder using 2,3,5,7 idf remiander is zero any case no is not prime)
#consider 9(divided 2 to8)
# num = int(input("Enter your number: "))
# if num <2:
#     print("its not in prime number range! ")
# else:
#     for i in range(2,num):
#         if num%i==0:
#             print(f"{num} is not prime")
#             break
#     else:
#         print(f"{num} is normal prime number")

#find the prime numbers in the range[10 to 30]
prime=[]
# for num in range(10,31):
#     if num<2 :
#         print("its not in prime number range! ")
#     else:
#         for i in range(2,num):
#             if num%i==0:
#                 break
#         else:
#             prime.append(num)
# print(prime)

#find count the prime numbers in the range[10 to 30]
# prime=[]
# for num in range(10,31):
#     if num<2 :
#         print("its not in prime number range! ")
#     else:
#         for i in range(2,num):
#             if num%i==0:
#                 break
#         else:
#             prime.append(num)
# print(len(prime))
# print(prime)

#input a number from user and reverse it(input->541,145)
num = 541
org=num
reverse=0
sum=0
while num >0:
    sum += num%10
    reverse = sum*10+10
    num = num//10
print(sum)
print(org)
#in first iteration n=541, digit 1, reverse (0*10+1)->1, num= 541//10->54
# n =54, digit =4 reverse = 1*10+4=>14 54//10==>5
# n=5 digit =5 revers 14*10+5=>145 n=0
#in 4th iteration cond False while loop breaks


#input a number from user and sum of numbers(input->541,(5+4+1))

num = 541
org=num
reverse=0
sum=0
while num >0:
    sum += num%10
    num = num//10
print(sum)
print(org)
#input string from user and removes remove duplicate

#input==programming->progamin

input_="programming"

#for i in input_:

#input two number from and swap it
a,b = 20,10
# find the largest number in the list without using index position
input_list = [100,10,-1,1200,11,3]





