# Hands-on Assignment 1
list_1 = [1,4,3,2,5]
for i in range(0, len(list_1)):
    print(list_1[i], sep=" ", end=" ")
print("\n")

# Hands-on Assignment 2
list_1.append(7)
for i in range(0, len(list_1)):
    print(list_1[i], sep=" ", end=" ")
print("\n")

# Hands-on Assignment 3
for i in range(0, len(list_1)//2):
    k = list_1[i]
    list_1[i] = list_1[len(list_1)-i-1]
    list_1[len(list_1)-i-1] = k
for i in range(0, len(list_1)):
    print(list_1[i], sep=" ", end=" ")
print("\n")

# Hands-on Assignment 4
print(list_1.count(3), end="\n\n")

# Hands-on Assignment 5
list_2 = []

for num in list_1:
    list_2.insert(0,num)

for i in range(0, len(list_2)):
    print(list_2[i], sep=" ", end=" ")
print("\n")

# Hands-on Assignment 6

list_1.insert(1,23)
for i in range(0, len(list_1)):
    print(list_1[i], sep=" ", end=" ")
print("\n")

# Hands-on Assignment 7
del list_1[-3]
for i in range(0, len(list_1)):
    print(list_1[i], sep=" ", end=" ")
print("\n")

# Hands-on Assignment 8
list_3 = [2,4,1,4,1,2,4,6,3,4,5,3,2,3,4,6,3,1,76,9,6,5,4]
list_3.remove(1)
for num in list_3:
    print(num, sep=" ", end=" ")
print("\n")
