class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Hash map? O(n) solution
        n = len(nums)
        map_hash = {}
        nums_diff = []
        
        for i in range(n):
            # Hash map array. Hash only if not in array; store index
            diff = target - nums[i]
            if diff in map_hash:
                if i != map_hash[diff]:
                    return [i, map_hash[diff]]
                
            map_hash[nums[i]] = i
            
        
       