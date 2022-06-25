class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        left_bound = self.search_left_bound(nums, target)
        res.append(left_bound)
        right_bound = self.search_right_bound(nums, target)
        res.append(right_bound)
        
        return res

    def search_left_bound(self, nums, target):
        # 左闭右闭
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = left + (right-left) / 2
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            elif target == nums[mid]:
                right = mid - 1
        
        # After while loop, left = right + 1; right = mid - 1; target = left?
        # if target greater than all num, then left will be right == len(nums)
        if left == len(nums):
            return -1
        
        # if target smaller than all num, then left = 0
        return -1 if target != nums[left] else left

    def search_right_bound(self, nums, target):
        # 左闭右闭
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = left + (right-left) / 2
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            elif target == nums[mid]:
                left = mid + 1
        
        # After while loop, left = right + 1; left = target + 1? right = target?
        # If target greater than all num, then left = len(nums); right = len(nums)
        # If target smaller than all num, then right = -1
        
        if right == -1:
            return -1
        return -1 if nums[right] != target else right

    