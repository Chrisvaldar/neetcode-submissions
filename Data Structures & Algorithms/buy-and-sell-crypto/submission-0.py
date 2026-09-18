class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        maxProf = 0

        for i in range(1,len(prices)):
            if prices[i] < minBuy:
                minBuy = prices[i]

            profit = prices[i] - minBuy
            if profit > maxProf:
                maxProf = profit

        return maxProf
