class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        max_count = 0
        i = 0
        count = 0
        
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                max_count = max(max_count, count)
                # Reset count to zero
                count = 0
                
            max_count = max(max_count, count)

        
        return max_count