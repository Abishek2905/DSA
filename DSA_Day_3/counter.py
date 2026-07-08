from collections import Counter
c = Counter([1,1,2,2,2,3,3,4,4,4,5,6,7])

print("Start Validating Counter \n")
print(f'Counter: {c}')
print(f'List of Counter: {list(c)}')
print(f'Check if number 2 is present: {c[2]}')
print(f'Check if number 9 is present: {c[9]}')
print(f'Print Elements: {list(c.elements())}')
print(f'Print Most Common: {c.most_common(3)}')
c.update([7,8,2])
print(f'Counter after update: {c}')
c.subtract([8,1,2])
print(f'Counter after subtract: {c}')
c2 = Counter([1,1,2,3,4,5])
print(f'Counter 1: {c}')
print(f'Counter 2: {c2}')
print(f'Counter 1 + Counter 2: {c + c2}')
print(f'Counter 1 - Counter 2: {c - c2}')
print(f'Counter 1 & Counter 2: {c & c2}')
print(f'Counter 1 | Counter 2: {c | c2}')


