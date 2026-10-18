class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first, second = heapq.heappop(stones), heapq.heappop(stones)
            if second > first:
                total = first - second
                heapq.heappush(stones, total)
        stones.append(0)
        return abs(stones[0])