from collections import namedtuple

Coordinates = namedtuple("Coordinates", ['x', 'y'])
print(Coordinates)

Axis = Coordinates(10, 20)
print(Axis)
print(Axis.x)
print(Axis.y)
print(Axis[0])
print(Axis[1])

Axis2 = Axis._replace(x=15)
print(Axis2)