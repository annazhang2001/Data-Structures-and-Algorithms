package leetcode.medium;

class Solution {
    public int minimumDeleteSum(String s1, String s2) {
        int m = s1.length();
        int n = s2.length();
        
        int[][] memo = new int[m][n];
        for (int[] row : memo) {
            Arrays.fill(row, -1);
        }
        
        return dp(memo, s1, 0, s2, 0);
        
    }
    
    public int dp(int[][] memo, String s1, int i, String s2, int j) {
        int res = 0;
        if (i == s1.length()) {
            int n = s2.length();
            for (; j < n; j++) {
                res += s2.charAt(j);
            }
            return res;
        }
        
        if (j == s2.length()) {
            int n = s1.length();
            for (; i < n; i++) {
                res += s1.charAt(i);
            }
            return res;
        }
        
        if (memo[i][j] != -1) {
            return memo[i][j];
        }
        
        if (s1.charAt(i) == s2.charAt(j)) {
            memo[i][j] = dp(memo, s1, i+1, s2, j+1);
        } else {
            memo[i][j] = Math.min(s1.charAt(i) + dp(memo, s1, i+1, s2, j), s2.charAt(j) + dp(memo, s1, i, s2, j+1));
        }
        
        return memo[i][j];
    }
    
    
}
