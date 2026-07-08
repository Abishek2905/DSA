from collections import (deque,
                        Counter,
                        OrderedDict,
                        defaultdict,
                        namedtuple)

x = deque([0,1,2])

print("Validating deque module\n")

print(list(x))
x.append(-1)
print(list(x))
x.appendleft(-2)
print(list(x))
print(x.pop())
print(x.popleft())
x.extend([3,4])
print(list(x))
x.extendleft([-2,-1])
print(list(x))
x.rotate(2)
print(list(x))
x.rotate(-1)
print(list(x))
print(len(x))
print(x[0])

print("\nSuccessfully validated deque module")