# import math
# num1 = 10
# print(id(num1), num1)
# num1 = num1 + 20
# num2 = 89
# print(id(num1), num1)
# print(num2 < num1)

# for count in range(1, 5, 2):
#     print('{}' .format(count), sep=' ', end=' ')
# sum = 0
# print(end='\n')
# for num in range(1, 51, 1):
#     sum += num
# print(sum)
# for letters in "Shashank":
#     print(letters, sep=' ', end=' ')
# print(end='\n')
# dictionary = {1: 'Shashank', 2: 'Shekhar'}
# for key in dictionary:
#     print(dictionary[key], sep=' ', end=' ')
# print(end='\n')
# s = ''
# for letters in s:
#     print(letters)
# else:
#     print("Empty String")
# num3 = 2
# if (num3 > 0):
#     print("positive")
# elif (num3 == 0):
#     print("zero")
# else:
#     print("negative")


# for num in range(1, 11, 1):
#     print(num, sep='\t', end=' ')
# print(end='\n')

# for number in range(10, 100, 1):
#     for r in range(2, int(math.sqrt(number))):  
#         flag = 1
#         if(number % r == 0):
#             #print(number, "is Not prime")
#             flag = -1
#             break
#     if (flag == 1):
#         print(number, "is Prime")
# number = 1221
# numcpy = number
# num2 = 0
# sum = 0
# while (number != 0):
#     sum = number%10
#     num2 = num2*10 + sum
#     number = number//10
# if (num2 == numcpy):
#     print("palindrome")
# else:
#     print("not palindrome")


# List ...............................................

# list1 = [1, 'abc', '#@$']

# print(list1[0:2])

# list1.append("Hello")
# del list1[-1]
# list1.remove(1)
# # list1.clear()
# # del list1

# str1 = 'hello'
# str1.upper()
# print(str1,id(str1))
# str2 = str1.upper()
# #print(str1,str2)
# str3 = str1[0:5]
# print(str3,id(str3))
