import heapq

heap = []
# Creating a heapqueue
heapq.heappush(heap,3)
heapq.heappush(heap,1)
heapq.heappush(heap,2)
print(heap)

heapq.heappop(heap)
print(heap)

heapq.heappushpop(heap,4)
print(heap)

heapq.heapreplace(heap,5)
print(heap)

arr = [3,1,4,1,5]
heapq.heapify(arr)
print(arr)
heapq.heappop(arr)
print(arr)