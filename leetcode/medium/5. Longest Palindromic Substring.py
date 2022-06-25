class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        lp_length = 0
        s_length = len(s)
        
        for i in range(s_length):
            
            # Odd
            r = i
            l = i
            
            while l >= 0 and r < s_length and s[r] == s[l]:
                if (r - l + 1) > lp_length:
                    lp_length = (r - l + 1)
                    res = s[l:r+1]
                r += 1
                l -= 1
            
            # Even
            l = i
            r = i + 1
            while l >= 0 and r < s_length and s[r] == s[l]:
                if (r - l + 1) > lp_length:
                    lp_length = (r - l + 1)
                    res = s[l:r+1]
                r += 1
                l -= 1
        
        return res