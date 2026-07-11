import random

print(random.random())
print(random.randint(1,10))
print(random.randrange(0,10,2))
print(random.choice(['yamaha', 'honda', 'suzuki']))
print(random.sample([1,4,2,3,6,5], 3))
print(random.uniform(1,10))

arr = [1,2,3,4,5]
random.shuffle(arr)
print(arr)

