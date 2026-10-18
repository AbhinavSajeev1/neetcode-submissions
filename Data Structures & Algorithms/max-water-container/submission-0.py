class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0
        l, r = 0, len(heights) - 1
        while l < r:
            current = (r-l) * min(heights[r], heights[l])
            if current > maxWater:
                maxWater = current

            if (heights[r] < heights[l]):
                r -= 1
            elif (heights[l] < heights[r]):
                l += 1
            elif (heights[l] == heights[r]):
                r-=1
                l+=1
        return maxWater

