from collections import OrderedDict

od = OrderedDict([('a',2),('Fruit','Apple'),('b',3),('c',4)])
print(od)
print(od['Fruit'])

od['Vegetable'] = 'Onion'
od['d'] = 5
print(od)

print(od.popitem())
print(od)
print(od.popitem(last=False))
print(od)

od.move_to_end('Fruit')
print(od)
od.move_to_end('c',last=False)
print(od)