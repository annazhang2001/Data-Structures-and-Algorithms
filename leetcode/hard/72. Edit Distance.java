package leetcode.hard;

class Solution {
    public int minDistance(String word1, String word2) {
        
        int m = word1.length();
        int n = word2.length();
        int[][] memo = new int[m][n];
        
        for (int[] row : memo) {
            Arrays.fill(row, -1);
        }
        
        return dp(memo, word1, m-1, word2, n-1);
    }
    
    // dp table: [0...i]; [0...j]
    // abcc abec
    public int dp(int[][] memo, String s1, int i, String s2, int j) {
        if (i < 0) {
            return j + 1;
        }
        if (j < 0) {
            return i + 1;
        }
        if (memo[i][j] != -1) {
            return memo[i][j];
        }
        
        if (s1.charAt(i) == s2.charAt(j)) {
            memo[i][j] = dp(memo, s1, i-1, s2, j-1);
        } else {
            memo[i][j] = min(1 + dp(memo, s1, i-1, s2, j), 1 + dp(memo, s1, i, s2, j-1),
                            1 + dp(memo, s1, i-1, s2, j-1));
        }
        
        return memo[i][j];
    }
    
    public int min(int a, int b, int c){
        return Math.min(Math.min(a, b), c);
    }
}

