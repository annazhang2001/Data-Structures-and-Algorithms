package leetcode.easy;

class Solution {
    public int[] plusOne(int[] digits) {
        int length = digits.length;
        
        int i = length - 1;
        while (i >= 0){
            int digit = digits[i];
            if (digit < 9) {
                digits[i]++;
                return digits;
            }
            // Carry
            else {
                if (i > 0){
                    digits[i] = 0;
                    i--;
                }
                // Need to resize
                else {
                    int[] newDigits = new int[length+1];
                    newDigits[0] = 1;
                    return newDigits;
                }
                
            }
        }
        
        return digits;
        
        
    }
}
