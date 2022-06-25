class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hash_map = {}
        
        for i in range(len(nums)):
            if nums[i] in hash_map and abs(hash_map[nums[i]] - i) <= k:
                return True
            hash_map[nums[i]] = i
                
        return False
        