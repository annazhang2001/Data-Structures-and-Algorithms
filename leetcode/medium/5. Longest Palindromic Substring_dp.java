package leetcode.medium;

class Solution {
    public String longestPalindrome(String s) {
        
        // DP approach
        int n = s.length();
        
        int[][] dp = new int[n][n];
        int length = 0;
        int[] sub = new int[2];
        
        for (int g = 0; g < n; g++) {
            for (int i = 0, j = g; j < n; i++, j++) {
                if (i == j) {
                    dp[i][j] = 1;
                } else if (j - i == 1) {
                    if (s.charAt(i) == s.charAt(j)) {
                        dp[i][j] = 2;
                    } else {
                        dp[i][j] = 0;
                    }
                } else {
                    if (s.charAt(i) == s.charAt(j) && dp[i+1][j-1] > 0) {
                        dp[i][j] = 1 + dp[i+1][j-1];
                    } else {
                        dp[i][j] = 0;
                    }
                }
                
                if (dp[i][j] > 0) {
                    if (j - i + 1 > length) {
                        length = j - i + 1;
                        sub[0] = i;
                        sub[1] = j;
                    }
                }
                
                
            }
        }
        
        return s.substring(sub[0], sub[1] + 1);
    
    }
}