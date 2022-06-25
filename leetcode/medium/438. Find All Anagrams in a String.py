class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
        needs = {}
        window = {}
        left = 0
        right = 0
        valid = 0
        length_s = len(s)
        length_p = len(p)
        res = []
        
        # Put stuff in p
        for letter in p:
            needs[letter] = needs.get(letter, 0) + 1
        
        # Sliding window
        # Expand window:
        while right < length_s:
            letter = s[right]
            right += 1
            # Put in window if part of anagram/p
            if letter in needs:
                window[letter] = window.get(letter, 0) + 1
                if window[letter] == needs[letter]:
                    valid += 1
                    
            if valid == len(needs):
                res.append(left)
                
            # shrink window
            while (right - left) == length_p:
                letter_left = s[left]
                left += 1
                
                if letter_left in needs:
                    if window[letter_left] == needs[letter_left]:
                        valid -= 1
                    window[letter_left] -= 1
        
        return res
                        
                
        
        