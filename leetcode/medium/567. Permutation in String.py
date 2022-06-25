class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        
        left = 0
        right = 0
        valid = 0
        needs = {}
        window = {}
        
        # Loop through s1
        for letter in s1:
            needs[letter] = needs.get(letter, 0) + 1
        
        
        # Expand window
        while right < len(s2):
            letter = s2[right]
            right += 1
            
            # Place into window if part of s1
            if letter in needs:
                window[letter] = window.get(letter, 0) + 1
                if window[letter] == needs[letter]:
                    valid += 1
            
            # Shrink window
            while (right - left) == len(s1):
                if valid == len(needs):
                    return True
                
                letter_left = s2[left]
                left += 1
                
                if letter_left in needs:
                    # Take out of window
                    if window[letter_left] == needs[letter_left]:
                        valid -= 1
                    window[letter_left] -= 1
                    
        return False
                
                
                
                
                
                
                
                