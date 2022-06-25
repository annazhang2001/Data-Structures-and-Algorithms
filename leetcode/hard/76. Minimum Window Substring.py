class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        needs = {}
        window = {}
        
        # valid is the number of letters in t that have been covered in s
        # 左闭右开
        
        valid = 0
        left = 0
        length = sys.maxint
        right = 0
        start = 0
        
        # Input t letters in needs
        for letter in t:
            needs[letter] = needs.get(letter, 0) + 1
        
        # Sliding window right, expand window
        while right < len(s):
            letter = s[right]
            right += 1
            
            # If this is a letter we need to cover
            if letter in needs:
                window[letter] = window.get(letter, 0) + 1
                if window[letter] == needs[letter]:
                    # All covered
                    valid += 1
            
            # Sliding window left, shrink window

            while valid == len(needs):
                if length > right - left:
                    start = left
                    length = right - left
                
                letter_left = s[left]
                left += 1
                
                if letter_left in needs:
                    if needs[letter_left] == window[letter_left]:
                        valid -= 1
                    window[letter_left] -= 1
        
        
        return "" if length == sys.maxint else s[start: start + length]
            
            
        
        
        
        
        
        