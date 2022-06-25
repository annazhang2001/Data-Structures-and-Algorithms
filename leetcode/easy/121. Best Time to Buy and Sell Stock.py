class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = sys.maxint
        max_profit = 0
        
        for i in range(len(prices)):
            price = prices[i]
            min_price = min(min_price, price)
            max_profit = max(price - min_price, max_profit)
        
        return max_profit
        