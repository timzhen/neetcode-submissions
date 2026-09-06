class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i,n in enumerate(prices):
            for m in prices[i:]:
                if (m - n) > profit:
                    profit = m - n



        return profit