class Solution(object):
 
        
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        # Bottom-up recursion
        memo = [-1] * (amount+1)
        
        memo[0] = 0
        
        for i in range(1, len(memo)):
            min = sys.maxint
            for coin in coins:
                if (i - coin) < 0:
                    continue 
                elif memo[i-coin] == -1:
                    continue
                    
                res = memo[i-coin]
                if (res + 1) < min:
                    min = res + 1
                
                memo[i] = -1 if min == sys.maxint else min
    
        return memo[amount]
        