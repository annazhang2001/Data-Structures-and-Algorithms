package leetcode.medium;

class Solution {
    public int maxSubArrayLen(int[] nums, int k) {
            
        if (nums.length == 0){
            return 0;
        }
        
        int length = 0;
        int curSum = 0;
        
        HashMap<Integer, Integer> map = new HashMap<>();
        map.put(0, -1);
        
        for (int i = 0; i < nums.length; i++){
            curSum += nums[i];
            if (map.containsKey(curSum-k)){
                int po_length = i - map.get(curSum-k);
                if (po_length > length){
                    length = po_length;
                }        
            }
            
            if (!map.containsKey(curSum)){
                map.put(curSum, i);
            }
        }
    
        return length;
            
        }
}