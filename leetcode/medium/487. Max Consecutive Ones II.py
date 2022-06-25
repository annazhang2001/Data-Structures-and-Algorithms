class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        count_1 = 0
        max_length = 0
        
        # Sliding window
        # 左闭右开
        left = 0
        right = 0
        n = len(nums)
        
        # Expand window
        while right <= n-1:
            if nums[right] == 1:
                count_1 += 1
            
            right += 1
            
            # Shrink window
            while (right - left) - count_1 > 1:
                if nums[left] == 1:
                    count_1 -= 1
                left += 1
            
            
            max_length = max(max_length, right-left)
        
        return max_length
        