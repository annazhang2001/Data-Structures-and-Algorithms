class Solution {
    public boolean isInterleave(String s1, String s2, String s3) {
        int m = s1.length();
        int n = s2.length();
        int k = s3.length();
        // Pre-check
        if (k != m + n) {
            return false;
        }

        // Recursive memoization
        int memo[][] = new int[m+1][n+1];
        for (int[] row : memo) {
            Arrays.fill(row, -1);
        }

        return dp(memo, s1, 0, s2, 0, s3);
    }

    boolean dp(int[][] memo, String s1, int i, String s2, int j, String s3) {
        int k = i + j;
        boolean res = false;
        if (k == s3.length()) {
            return true;
        }
        if (memo[i][j] != -1) {
            return memo[i][j] == 1 ? true : false;
        }
        if (i < s1.length() && s1.charAt(i) == s3.charAt(k)) {
            res = dp(memo, s1, i+1, s2, j, s3);
        }
        if (j < s2.length() && s2.charAt(j) == s3.charAt(k)) {
            res = res || dp(memo, s1, i, s2, j+1, s3);
        }
        memo[i][j] = (res == true) ? 1 : 0;
        return res;
    }
}