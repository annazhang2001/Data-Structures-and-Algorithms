class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        need = 0
        res = 0
        i = 0
        
        for i in range(len(s)):
            if s[i] == "(":
                need += 2
                if need % 2 == 1:
                    res += 1
                    need -= 1
            elif s[i] == ")" and need > 0:
                need -= 1
            elif s[i] == ")" and need == 0:
                res += 1
                need += 1
            
        return need + res