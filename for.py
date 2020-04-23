import math

# Hands-on Assignment 4

for num in range(1, 11, 1):
    print(num, sep='\t', end=' ')
print(end='\n')
print(end='\n')


# Hands-on Assignment 5

for num in range(23,57,1):
    if(num%2 == 0):
        print(num)
print(end='\n')


# Hands-on Assignment 6

num = 113
flag = 1

for r in range(2, int(math.sqrt(num))):
    if(num%r == 0):
        flag = -1
        break
if (flag == 1):
    print("Prime")
else:
    print("Not Prime")
print(end='\n')



# Hands-on Assignment 7

for number in range(10, 100, 1):
    for r in range(2, int(math.sqrt(number))):  
        flag = 1
        if(number % r == 0):
            #print(number, "is Not prime")
            flag = -1
            break
    if (flag == 1):
        print(number, "is Prime")
print(end='\n')

