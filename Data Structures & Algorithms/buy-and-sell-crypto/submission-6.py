class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPrice = 0
        l, r = 0, 1

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxPrice = max(maxPrice, profit)
            elif prices[l] >= prices[r]:
                l = r
            r += 1
        return maxPrice