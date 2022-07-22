package leetcode.medium;

class Solution {
    public int minDistance(String word1, String word2) {
        int lcsLength = LCS(word1, word2);
        
        return word1.length() + word2.length() - 2 * lcsLength;
    }
    
    public int LCS(String s1, String s2) {
        int m = s1.length();
        int n = s2.length();
        
        int[][] dp = new int[m+1][n+1];
        
        for (int i = 1; i < m+1; i++) {
            for (int j = 1; j < n+1; j++) {
                if (s1.charAt(i-1) == s2.charAt(j-1)) {
                    dp[i][j] = dp[i-1][j-1] + 1;
                } else {
                    dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);
                }
                
            }
        }
        
        return dp[m][n];
        
    }
    
}