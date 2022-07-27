class Solution {
    public int maxProfit(int[] prices) {
        
        // 状态压缩
        int days = prices.length;
        
        int dp_0 = 0;
        int dp_1 = -prices[0];
        
        for (int i = 1; i < days; i++) {
            int tmp = dp_0;
            dp_0 = Math.max(dp_0, dp_1 + prices[i]);
            dp_1 = Math.max(dp_1, tmp - prices[i]);    
        }
        
        return dp_0;
    }
}