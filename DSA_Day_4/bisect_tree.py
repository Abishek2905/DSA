import bisect

arr = [1,3,3,4,5,6,7]
print(bisect.bisect_right(arr,4))
print(bisect.bisect_left(arr,2))

print(bisect.bisect(arr,4))

bisect.insort_left(arr,2)
print(arr)

print(bisect.bisect_right(arr,4))
bisect.insort_right(arr,4)
print(arr)

bisect.insort(arr,7)
print(arr)