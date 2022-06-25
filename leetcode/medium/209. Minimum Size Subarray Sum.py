class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        
        left = 0
        right = 0
        current_sum = 0
        length = sys.maxint
        
        # Expand window
        while right < len(nums):
            current_sum += nums[right]
            right += 1
            
            # Shrink window
            while current_sum >= target:
                if length > right - left:
                    length = right - left
                    
                current_sum -= nums[left]
                left += 1
        
        return 0 if length == sys.maxint else length