set_1 = {1,2,3,4}
print(f' Printing Set: {set_1}')

set_1.add(5)
print(f' Printing Set: {set_1}')

set_1.remove(2)
print(f' Printing Set: {set_1}')

set_1.discard(3)
print(f' Printing Set: {set_1}')

set_1.discard(10) # This will not raise an error since discard does not throw an error if the element is not found.
print(f' Printing Set: {set_1}')

set_1.pop()
print(f' Printing Set: {set_1}')

set_2 = set_1.copy()
print(f' Printing Set2: {set_2}')

set_1.clear()
print(f' Printing Set1: {set_1}')
print(f' Printing Set2: {set_2}')

print(f' Check if 1 exists in Set2: {1 in set_2}')

# print(f' Removing 10 from Set2: {set_2.remove(10)}') # This will raise a KeyError since 10 is not in the set.

# Set Operations 
s1 = {1,2,3}
s2 = {3,4,5}

print(f' Union of s1 and s2: {s1.union(s2)}')
print(f' Intersection of s1 and s2: {s1.intersection(s2)}')
print(f' Difference of s1 and s2: {s1.difference(s2)}')
print(f' Symmetric Difference of s1 and s2: {s1.symmetric_difference(s2)}')
print({1,2}<=s1)
print(s1>={1,2,4})

