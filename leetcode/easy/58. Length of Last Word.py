class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        end = len(s) - 1
        length = 0
        
        # Find the first non space char
        while s[end] == " ":
            end -= 1
        
        # Count word length
        while end >= 0 and s[end] != " ":
            length += 1
            end -= 1
        
        return length
        