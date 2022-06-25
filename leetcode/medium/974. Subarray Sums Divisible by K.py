class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        sub_count = 0
        remainders = {0: 1}
        
        curSum = 0 
    
        for i in range(len(nums)):
            curSum += nums[i]
            remainder = curSum % k
            
            if remainder in remainders:
                sub_count += remainders[remainder]
            
            remainders[remainder] = remainders.get(remainder, 0) + 1
        
        return sub_count