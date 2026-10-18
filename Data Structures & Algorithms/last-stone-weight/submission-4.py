class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1: 
            first, second = heapq.heappop_max(stones), heapq.heappop_max(stones)
            if first > second:
                difference = first - second
                heapq.heappush_max(stones, difference)
            elif second > first:
                difference = second - first
                heapq.heappush_max(stones, difference)
        stones.append(0)
        return stones[0]
            