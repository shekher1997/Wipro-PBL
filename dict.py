# Hands-on Assignment 1

dict1 = {1:'A', 2:'B'}
dict1[3] = 'C'
print(dict1)
print(end="\n")

# Hands-on Assignment 2

dictA = {1:10, 2:20}
dictB = {3:30, 4:40}
dictC = {4:40, 5:50, 6:60}

for keys in dictB:
    dictA[keys] = dictB[keys]

for keys in dictC:
    dictA[keys] = dictC[keys]

print(dictA)
print(end="\n")

# Hands-on Assignment 3

if 4 in dictA:
    print("Present")
    print(end="\n")

# Hands-on Assignment 4

for keys in dictA:
    print(keys, sep=" ", end=" ")
print(end="\n\n")

for keys in dictA:
    print(dictA[keys], sep=" ", end=" ")
print(end="\n\n")

for keys in dictA:
    print(keys, end=" = ")
    print(dictA[keys], sep='', end='\n')
print(end="\n")

# Hands-on Assignment 5
dictD = {}
for keys in range(1,16,1):
    dictD[keys] = keys**2
print(dictD, end="\n\n")

# Hands-on Assignment 6

sum = 0
for keys in dictD:
    sum = sum + dictD[keys]
print(sum)

    