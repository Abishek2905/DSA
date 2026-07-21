new_dict = {'a': 1, 'b': 2}

print(f' Printing Dictionary: {new_dict}')
print(f"Value of key 'a': {new_dict['a']}")

print(f"Value of key 'b': {new_dict.get('b')}")

print(f"Value of key 'c': {new_dict.get('c',0)}")

new_dict['c'] = 3
print(f' Printing Dictionary: {new_dict}')

new_dict.update({'d': 4})
print(f' Printing Dictionary: {new_dict}')

new_dict.pop('a')
print(f' Printing Dictionary: {new_dict}')

new_dict.popitem()
print(f' Printing Dictionary: {new_dict}')

print(f'Check if x exists and pop and if not return -1: {new_dict.pop("x", -1)}')

new_dict.clear()
print(f' Printing Dictionary: {new_dict}')

dict2 = {'a': 1, 'b': 2}
dict3 = dict2.copy()
print(f' Printing Dictionary2: {dict2}')
print(f' Printing Dictionary3: {dict3}')

print(f'Check if key "a" exists in dict2: {"a" in dict2}')

print(list(dict2.keys()))
print(list(dict2.values()))
print(list(dict2.items()))

dict2['c'] = 3
print(f' Printing Dictionary2: {dict2}')
print(f' Printing Dictionary3: {dict3}')