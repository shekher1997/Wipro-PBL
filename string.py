# Hands-on Assignment 1

string = 'abVdGdsSvDgdDeD'
isupper = 0
islower = 0
for letters in string:
    if(letters.isupper()):
        isupper += 1
    else:
        islower += 1
print(isupper, " ", islower, end="\n\n")

# Hands-on Assignment 2

string = 'maddam'
flag = 1
for a in range(0,len(string)//2,1):
    if (string[a] != string[len(string)-a-1]):
        flag = -1
        break
if (flag == 1):
    print("Palindrome")
else:
    print("Not palindrome")
print(end="\n")

# Hands-on Assignment 3

string = 'Mirai'
string2 = str()
for i in range(0,len(string),1):
    string2 = string2 + string[0] + string[1]

print(string2, end="\n\n")

# Hands-on Assignment 4

string = 'xHix'
string2 = str()
 
for letters in string:
    if (letters != 'x'):
        string2 = string2 + letters
print(string2, end="\n\n")

# Hands-on Assignment 5

string = 'Wipro'
n = 3
string2 = str()
for i in range(0,3,1):
    for k in range(-1*n,0,1):
        string2 += string[k]
print(string2)