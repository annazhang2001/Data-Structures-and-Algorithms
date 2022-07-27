package leetcode.medium;

class Solution {
    
    public int rob(int[] nums) {
    
        if (nums.length == 1) {
            return nums[0];
        }
        
        int n = nums.length;
        return Math.max(robHelper(nums, 0, n-2), robHelper(nums, 1, n-1));
        
    }
    
    public int robHelper(int[] nums, int start, int end) {
        if (start == end) {
            return nums[start];
        }
        if (start > end) {
            return 0;
        }
        
        int dp_2 = nums[start];
        int dp_1 = Math.max(nums[start], nums[start+1]);
        
        for (int i = start+2; i <= end; i++) {
            int dp = Math.max(dp_2 + nums[i], dp_1);
            dp_2 = dp_1;
            dp_1 = dp;
        }
        
        return dp_1;
    }
    
}