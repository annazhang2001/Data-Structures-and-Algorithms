class Solution {
    public boolean isInterleave(String s1, String s2, String s3) {
        int m = s1.length();
        int n = s2.length();
        int k = s3.length();
        // Pre-check
        if (k != m + n) {
            return false;
        }

        // Dynamic programming
        boolean dp[][] = new boolean [m + 1][n + 1];
        for (int i = m; i >= 0; i--) {
            for (int j = n; j >= 0; j--) {
                if (i == m && j == n) {
                    dp[i][j] = true;
                } else if (i < m && s1.charAt(i) == s3.charAt(i+j) && dp[i+1][j]) {
                    dp[i][j] = true;
                } else if (j < n && s2.charAt(j) == s3.charAt(i+j) && dp[i][j+1]) {
                    dp[i][j] = true;
                }
            }
        }

        return dp[0][0];
        
    }
}