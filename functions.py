# Hands-on Assignment 1

def sumList(listInput):
    sum1 = 0
    for elements in listInput:
        sum1 += elements
    return sum1

list1 = [2,5,8,4,5,7,4,8,4,5,78,54]
print(sumList(list1),end="\n\n")

# Hands-on Assignment 2

string = '1234abcd@#'

def reverse(string):
    strrev = str()
    for letters in string:
        strrev = letters + strrev
    print(strrev, end="\n\n")

reverse(string)

# Hands-on Assignment 3

def factorial(integer):
    if(integer > 0):
        fact = 1
        while (integer != 1):
            fact *= integer
            integer -= 1
        return fact
    elif (integer == 0):
        return 1
    else:
        return "Non Positive Value!!!"

print(factorial(7), end="\n\n")


# Hands-on Assignment 4

string = 'AfdDfgEsGhHH'

def count(string):
    isUpper = 0
    isLower = 0
    for letters in string:
        if (letters.isupper()):
            isUpper += 1
        else:
            isLower +=1
    print("Upper Case = ",isUpper,"\nLower Case = ",isLower, end="\n\n")

count(string)

# Hands-on Assignment 5

def evenlist(listInput):
    listeven = list()
    for elements in listInput:
        if (elements%2 == 0):
            listeven.append(elements)
    return listeven

print(evenlist(list1), end="\n\n")

# Hands-on Assignment 6

import math
def primecheck(integer):
    flag = 1
    for i in range(2,int(math.sqrt(integer)),1):
        if(integer%i == 0):
            flag = -1
            break
    if (flag == 1):
        print("Prime", end="\n\n")
    else:
        print("Not Prime", end="\n\n")

primecheck(51)
primecheck(113)