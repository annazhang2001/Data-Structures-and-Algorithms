class Solution {
    public void sortColors(int[] nums) {
        
        // Three pointers
        
        int p0 = 0;
        int p2 = nums.length - 1;
        int cur = 0;
        
        while (cur <= p2) {
            if (nums[cur] == 0) {
                swap(p0++, cur++, nums);
            } else if (nums[cur] == 1) {
                cur++;
            } else {
                swap(p2--, cur, nums);
            }
        }
    }
    
    private void swap(int pos1, int pos2, int[] nums) {
        int tmp = nums[pos1];
        nums[pos1] = nums[pos2];
        nums[pos2] = tmp;
    }
}