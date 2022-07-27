package leetcode.medium;

class Solution {
    public int findLength(int[] nums1, int[] nums2) {
        
        // [0 ... i]; [0 ... j]
        // max length of repeated subarray that ends with both i and j
        // if i == j --> 1 + prev
        // else : 0
        
        int m = nums1.length;
        int n = nums2.length;
        
        int[][] dp = new int[m][n];
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 || j == 0) {
                    dp[i][j] = (nums1[i] == nums2[j]) ? 1 : 0;
                    continue;
                }
                
                if (nums1[i] == nums2[j]) {
                    dp[i][j] = 1 + dp[i-1][j-1];
                } else {
                    dp[i][j] = 0;
                }
                
            }
        }
        
        int max = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                max = Math.max(max, dp[i][j]);
            }
        }
        
        return max;
    }
}