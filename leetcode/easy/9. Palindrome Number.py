class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        if x < 0: return False

        # Flip the entire number
        flip_num = 0
        num = x
        
        while x > 0:
            digit = x % 10
            flip_num = flip_num * 10 + digit
            x /= 10
       
        return num == flip_num
        