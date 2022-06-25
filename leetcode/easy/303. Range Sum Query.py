class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.prefixSum = []
        self.prefixSum.append(0)
        
        for i in range(1, len(nums)+1):
            self.prefixSum.append(self.prefixSum[i-1] + nums[i-1])
        
    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.prefixSum[right+1] - self.prefixSum[left]
