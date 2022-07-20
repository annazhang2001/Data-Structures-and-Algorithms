package leetcode.medium;

class Solution {
    public int minFallingPathSum(int[][] matrix) {
        
        int n = matrix.length;
        
        int[][] dp = new int[n][n];
    
        for (int i = 0; i < n; i++){
            for (int j = 0; j < n; j++){
                
                if (i == 0){
                    dp[i][j] = matrix[i][j];
                    continue;
                }
                
                int topL = findNum(dp, i-1, j-1);
                int topR = findNum(dp, i-1, j+1);
                int top = findNum(dp, i-1, j);
                
                int sum = matrix[i][j] + Math.min(Math.min(topL, topR), Math.min(topR, top));
                
                dp[i][j] = sum;
                
            }
        }
        
        int min = dp[n-1][0];

        for (int i = 0; i < n; i++){
            min = Math.min(min, dp[n-1][i]);
        }
        return min;
    }
    
    public int findNum(int[][] dp, int i, int j){
        int n = dp.length;
        if (i < 0 || j < 0 || i >= n || j >= n){
            return 99999;
        }
        
        return dp[i][j];
    }
}