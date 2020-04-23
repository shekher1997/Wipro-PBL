# Hands-on Assignment 8

num = 1234
sum = 0
while (num != 0):
    sum += num%10
    num //= 10
print(sum)
print(end="\n")

# Hands-on Assignment 9

num = 23413
i = 0
k = ""
while (i != len(str(num))):
    k = str(num)[i] + k
    i += 1
print(int(k))
print("\n", end="")

# Or
length = len(str(num))
i = 1
while (i < length):
    num = (num + ((num//(10**(i-1)))%10)*(10**(2*length-i-1)))
    i += 1
num //= 10**(length-1)
print(num)
print(end="\n")

# Or

num = 23413
rev = 0
while(num != 0):
    rev = rev*10 + num%10
    num = num//10
print(rev)
print(end="\n")

# Hands-on Assignment 8

num = 1221
numcpy = num
length = len(str(num))
i = 1
while (i < length):
    num = (num + ((num//(10**(i-1)))%10)*(10**(2*length-i-1)))
    i += 1
num //= 10**(length-1)

if (num == numcpy):
    print("Palindrome")
else:
    print("Not Plaindrome")
