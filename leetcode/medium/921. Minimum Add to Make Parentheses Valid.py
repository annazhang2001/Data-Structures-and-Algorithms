class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        need = 0
        left = 0
        
        for i in range(len(s)):
            if s[i] == "(":
                need += 1
            elif s[i] == ")" and need > 0:
                need -= 1
            elif s[i] == ")" and need == 0:
                left += 1
        
        return need + left
            
        