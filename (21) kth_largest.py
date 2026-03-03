import heapq
def kth_largest(nums,k):
    heap = []
    
    for num in nums:
        heapq.heappush(heap,num)
        
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]
        
print(kth_largest([3,2,1,5,6,4] , 1))
