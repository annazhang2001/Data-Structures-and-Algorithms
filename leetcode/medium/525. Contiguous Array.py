class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        count = 0
        maxLength = 0
        
        map = {0: -1}
        
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count -= 1
            
            if count in map:
                maxLength = max(maxLength, i - map[count])
            else:
                map[count] = i
        
        return maxLength