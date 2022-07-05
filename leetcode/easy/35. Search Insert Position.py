class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        def left_bound(nums, target):
            left = 0
            right = len(nums)
            
            while left < right:
                mid = left / 2 + right / 2
                if nums[mid] == target:
                    right = mid
                elif nums[mid] > target:
                    right = mid
                elif nums[mid] < target:
                    left = mid + 1
            
            return left
        
        return left_bound(nums, target)