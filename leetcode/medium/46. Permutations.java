package leetcode.medium;

class Solution {
    
    
    // With optimization
    
    List<List<Integer>> res = new LinkedList<>();
    
    public List<List<Integer>> permute(int[] nums) {
        ArrayList<Integer> nums_lst = new ArrayList<>();
        for (int i : nums){
            nums_lst.add(i);
        }
        
        backtrack(nums.length, nums_lst, 0);
        return res;
        
    }
    
    public void backtrack(int n, ArrayList<Integer> nums, int first){
        if (first == n){
            res.add(new ArrayList(nums));
        }
        
        for (int i = first; i < n; i++){
            Collections.swap(nums, first, i);
            backtrack(n, nums, first+1);
            Collections.swap(nums, first, i);
        }
    }
    
   
}