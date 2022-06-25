class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        hash_num = {}
        for num in nums:
            if num not in hash_num:
                hash_num[num] = 1
            else:
                return True

        return False