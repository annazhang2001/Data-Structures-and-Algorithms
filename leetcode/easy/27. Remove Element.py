class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        
        slow = 0
        fast = 0
        
        while fast < n:
            if nums[fast] != val:
                # Swap
                #tmp = nums[slow]
                nums[slow] = nums[fast]
                #nums[fast] = tmp
                slow += 1
            fast += 1
        
        return slow