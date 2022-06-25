class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        max_length = 0
        hash_map = {}
        right = 0
        left = 0
        
        # Sliding window
        # Expand window
        while right < len(s):
            letter_right = s[right]
            right += 1
            
            # Put into hash map
            hash_map[letter_right] = hash_map.get(letter_right, 0) + 1
            
            # shrink window
            while hash_map[letter_right] > 1:
                letter_left = s[left]
                left += 1
                hash_map[letter_left] -= 1
            
            if max_length < (right - left):
                max_length = (right - left)
        
        return max_length
                
                
        
        