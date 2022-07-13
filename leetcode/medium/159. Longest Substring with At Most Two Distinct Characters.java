package leetcode.medium;

class Solution {
    public int lengthOfLongestSubstringTwoDistinct(String s) {
        
        if (s.length() == 0){
            return 0;
        }
        
        // [left, right)
         
        int left = 0;
        int right = 0;
        int length = 0;
        HashMap<Character, Integer> map = new HashMap<>();
        
        // Expanding
        while (right < s.length()){
            char rightChar = s.charAt(right);
            right++;
            map.put(rightChar, map.getOrDefault(rightChar, 0) + 1);
            
            // Shrinking
            while (map.size() > 2){
                char leftChar = s.charAt(left);
                map.put(leftChar, map.get(leftChar)-1);
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