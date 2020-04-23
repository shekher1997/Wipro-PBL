# Hands-on Assignment 1

tuple1 = (1,2,3,4,5,6,7,8,9,10)

print(tuple1[3])
print(tuple1[-4])
print(end='\n')

# Hands-on Assignment 2

if 1 in tuple1:
    print("Exist")
else:
    print("Doesn't Exist")

print(end='\n')

# Hands-on Assignment 3


list1 = [1,2,3,4,5,6,7,8,9,10]
list1 = tuple(list1)
print(type(list1))
print(end='\n')

# Hands-on Assignment 4  

tupleA = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p')
tupleA = list(tupleA)

print(tupleA.index('d'), end="\n\n")

# Hands-on Assignment 5

list2 = [(20,40,34), (23,54,64), (43,23,44)]

for i in range(0,len(list2),1):
    list2[i] = list(list2[i])
    list2[i][-1] = 100
    list2[i] = tuple(list2[i])

print(list2)
print(end="\n")

