package leetcode.hard;

class Solution {
    public int calculateMinimumHP(int[][] dungeon) {
        int m = dungeon.length;
        int n = dungeon[0].length;
        
        int[][] dp = new int[m+1][n+1];
        
        dp[m-1][n-1] = dungeon[m-1][n-1] >= 0 ? 1 : -dungeon[m-1][n-1] + 1;
        
        for (int i = m; i >= 0; i--) {
            for (int j = n; j >= 0; j--) {
                if (i == m-1 && j == n-1) {
                    continue;
                } else if (i == m || j == n) {
                    dp[i][j] = Integer.MAX_VALUE;
                    continue;
                } else {
                    int res = Math.min(dp[i][j+1], dp[i+1][j]) - dungeon[i][j];
                    dp[i][j] = res <= 0 ? 1 : res;
                }
            }
        }
        
        return dp[0][0];
        
        
    }
}