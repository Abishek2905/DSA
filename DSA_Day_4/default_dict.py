from collections import defaultdict


dd = defaultdict(int)
print(dd)
dd['a']
print(dd['a'])
dd['a'] += 1
print(dd['a'])

dd_list = defaultdict(list)
dd_list['bikes'].append('Yamaha')
print(dd_list['bikes'])
dd_list['bikes'].append('Honda')
print(dd_list['bikes'])
print(dd_list['cars'])
print(dd_list)

dd_set = defaultdict(set)
dd_set['num']
print(dd_set['num'])
dd_set['num'].add(1)
print(dd_set['num'])
dd_set['num'].add(2)
print(dd_set['num'])
dd_set['num'].add(1)
print(dd_set['num'])
print(dd_set)

dd_unique = defaultdict(lambda: "N/A")
dd_unique['email']
print(dd_unique['email'])
print(dd_unique)