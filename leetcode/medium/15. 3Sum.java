class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        int n = nums.length;
        List<List<Integer>> res = new LinkedList<>();
        for (int i = 0; i < n && nums[i] <= 0; i++) {
            twoSum(nums, i, res);
            while (i < n-1 && nums[i] == nums[i+1]) {
                i++;
            }
        }
        
        return res;
        
        
    }
    
    public void twoSum(int[] nums, int i, List<List<Integer>> res) {
        int lo = i + 1;
        int hi = nums.length - 1;
        
        while (lo < hi) {
            int left = nums[lo], right = nums[hi];
            int sum = left + right + nums[i];
            if (sum > 0) {
                while ((lo < hi && nums[hi] == right)) {
                    hi--;
                }
            } else if (sum < 0) {
                while ((lo < hi && nums[lo] == left)) {
                    lo++;
                }
            } else {
                res.add(Arrays.asList(nums[i], left, right));
                while (lo < hi && nums[lo] == left) lo++;
                while (lo < hi && nums[hi] == right) hi--;
            }
        }
        
    }
    
}
