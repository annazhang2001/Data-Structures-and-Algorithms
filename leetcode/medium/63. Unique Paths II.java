class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int m = obstacleGrid.length;
        int n = obstacleGrid[0].length;

        int dp[] = new int[n];
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 && j == 0) {
                    dp[j] = 1 - obstacleGrid[0][0];
                } else if (obstacleGrid[i][j] == 1) {
                    dp[j] = 0;
                    continue;
                } else {
                    if (j == 0) {
                        dp[j] = dp[j];
                    } else {
                        dp[j] = dp[j] + dp[j-1];
                    }
                }
            }
        }

        return dp[n-1];
    }
}