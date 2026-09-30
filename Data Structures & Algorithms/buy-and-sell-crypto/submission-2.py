class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        l, r = 0, 1

        while r < len(prices):
            profit = prices[r] - prices[l]

            if profit > 0:
                maxP = max(maxP, profit)
                r += 1
            else:
                l = r
                r += 1
        return maxP