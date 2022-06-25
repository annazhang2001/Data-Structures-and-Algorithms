class Solution(object):
 
        
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        # Top-Down with Recursion
        
        memo = [0] * (amount+1)
        memo[0] = 0
        
        return self.dp(coins, amount, memo)
        
    def dp(self, coins, amount, memo):
        
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        
        if memo[amount] != 0:
            return memo[amount]
        
        min = sys.maxint

        for coin in coins:  
            res = self.dp(coins, amount-coin, memo)
            if res >= 0 and res < min:
                min = res + 1
        
        memo[amount] = -1 if min == sys.maxint else min
        
        return memo[amount]
        
        
        
        
        
        
        