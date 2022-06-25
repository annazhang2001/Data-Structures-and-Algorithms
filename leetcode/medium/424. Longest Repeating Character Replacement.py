class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        right = 0
        left = 0
        
        windows = {}
        
        max_length = 0
        maxf = 0
        
        n = len(s)
        
        # 左闭右开
        while right <= n - 1:
            letter_right = s[right]
            right += 1
            
            windows[letter_right] = windows.get(letter_right, 0) + 1
            if maxf < windows[letter_right]:
                maxf = windows[letter_right]
            
            # Shrink window
            while right - left - maxf > k:
                letter_left = s[left]
                windows[letter_left] -= 1
                left += 1
            
            max_length = max(max_length, right-left)
        
        return max_length
                
                