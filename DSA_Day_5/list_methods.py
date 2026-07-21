lst = [1,2,3,4]

print(f' Printing List: {lst}')

lst.append(5)
print(f' Printing List: {lst}')

lst.extend([4,6])
print(f' Printing List: {lst}')

lst.insert(-1,1)
print(f' Printing List: {lst}')

lst.remove(2)
print(f' Printing List: {lst}')

lst.pop()
print(f' Printing List: {lst}')

lst.pop(-1)
print(f' Printing List: {lst}')

print(f' Index of 4: {lst.index(4)}')

print(f' Count of 5: {lst.count(5)}')

lst.sort()
print(f' Printing List: {lst}')

lst.sort(reverse=True)
print(f' Printing List: {lst}')

lst.reverse()
print(f' Printing List: {lst}')

lst.clear()
print(f' Printing List: {lst}')

lst2 = [1,2,3,4]
lst3 = lst2.copy()
print(f' Printing List3: {lst3}')
lst2.append(5)
print(f' Printing List2: {lst2}')
print(f' Printing List3: {lst3}')
