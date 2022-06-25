class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        # 左闭右闭
        left = 0
        right = len(nums) - 1
       
        while left <= right:
            mid = left + (right-left) / 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
        
        return -1
            