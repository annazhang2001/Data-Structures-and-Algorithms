package leetcode.easy;

class Solution {
    
    public String longestCommonPrefix(String[] strs) {
        
        if (strs.length == 0){
            return "";
        }
        
        int counter = 0;
        char curChar = 'a';
        
        int max_length = strs[0].length();
        
        while (counter < max_length){
            curChar = strs[0].charAt(counter);
            for (int i = 1; i < strs.length; i++){
                
                if (counter >= strs[i].length()){
                    return strs[i].substring(0, counter);
                }
                
                char newChar = strs[i].charAt(counter);
                if (newChar != curChar){
                    return strs[i].substring(0, counter);
                }
            }
            
            counter++;
            
        }
        
        return strs[0].substring(0, counter);
        
    }
}