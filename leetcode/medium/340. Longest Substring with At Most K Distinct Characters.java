package leetcode.medium;

class Solution {
    public int lengthOfLongestSubstringKDistinct(String s, int k) {
    
        if (s.length() == 0){
            return 0;
        }
        
        int left = 0;
        int right = 0;
        int length = 0;
        
        HashMap<Character, Integer> map = new HashMap<>();
        
        while (right < s.length()){
            char rightChar = s.charAt(right);
            right++;
            map.put(rightChar, map.getOrDefault(rightChar, 0) + 1);
            
            while (map.size() > k){
                char leftChar = s.charAt(left);
                map.put(leftChar, map.get(leftChar) - 1);
                if (map.get(leftChar) == 0){
                    map.remove(leftChar);
                }
                left++;
            }
            
            if (right-left > length){
                length = right-left;
            }
            
        }
        
        return length;
        
    }
}