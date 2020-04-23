# Hands-on Assignment 1

set_1 = {1,2,3,4,5}
set_1.remove(3)
print(set_1, end="\n\n")

# Hands-on Assignment 2

set_1 = {1,2,3,4,5,6,7}
set_2 = {4,5,6,7,8,9,10}
set_inter = set()

for elements in set_1:
    if elements in set_2:
        set_inter.add(elements)
        #print(elements)
print(set_inter, end="\n\n")

# Hands-on Assignment 3

set_union = set()
for elements in set_1:
    set_union.add(elements)
for elements in set_2:
    if elements not in set_union:
        set_union.add(elements)
print(set_union, end="\n\n")

# Hands-on Assignment 4

print(max(set_union))
print(min(set_union))
