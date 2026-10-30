class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [-i for i in nums]
        heapq.heapify(max_heap)

        val = 0
        while True:
            if k == 0:
                return val
            val = (heapq.heappop(max_heap)) * -1
            k -= 1
        
            
