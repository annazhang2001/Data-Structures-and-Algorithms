class Solution {
    public int longestConsecutive(int[] nums) {
        
        if (nums.length == 0) {
            return 0;
        }
        
        HashSet<Integer> set = new HashSet<>();
        int maxSeq = 0;
        int curNum = 0;
        int curSeq = 0;
        
        for (int i : nums) {
            set.add(i);
        }
        
        for (int num : set) {
            
            // Check if part of the sequence
            if (!set.contains(num-1)) {
                curNum = num;
                curSeq = 1;
            }
            
            while (set.contains(curNum+1)) {
                curNum++;
                curSeq++;
            }
            
            maxSeq = Math.max(maxSeq, curSeq);
        }
        
        return maxSeq;
        
    }
}