class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # Top down
        bank = {}
        
        def count(n):
            if n == 0 or n == 1:
                return 1
            if n in bank:
                return bank[n]
            res = 0
            for i in range(1, n+1):
                left = i-1
                right = n-i
                sub_left = count(left)
                sub_right = count(right)
                
                res += sub_left * sub_right
                
            bank[n] = res
            return res
        
        return count(n)