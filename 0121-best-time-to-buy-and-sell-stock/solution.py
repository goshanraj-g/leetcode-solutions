class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0
        l = 0
        r = 1
        while r < len(prices):
            if prices[l] >= prices[r]:
                l = r
                r += 1
            else:
                max_profit = max((prices[r]-prices[l], max_profit))
                r += 1
        return max_profit
