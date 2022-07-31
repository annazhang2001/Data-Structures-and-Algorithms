class Solution {
    public int jump(int[] nums) {
        
        int n = nums.length;
        
        // Greedy
        int end = 0;
        int farthest = 0;
        int count = 0;
        
        for (int i = 0; i < n - 1; i++) {
            farthest = Math.max(farthest, i + nums[i]);
            
            if (end == i) {
                count++;
                end = farthest;
            }
        }
        
        return count;
        

    }
}