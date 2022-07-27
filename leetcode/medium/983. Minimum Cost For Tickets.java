
class Solution {
    int[] memo;
    public int mincostTickets(int[] days, int[] costs) {
        memo = new int[days.length];
        Arrays.fill(memo, -1);
        return dp(0, days, costs);
    }
    
    public int dp(int start, int[] days, int[] costs) {
        int n = days.length;
        
        if (start >= n) {
            return 0;
        }
        if (memo[start] != -1) {
            return memo[start];
        }
        
        int start_date = days[start];
        int one = start + 1;
        int seven = 366;
        int thirty = 366;
        
        for (int i = start + 1; i < n; i++) {
            if (days[i] >= start_date + 7 && seven == 366) {
                seven = i;
            } else if (days[i] >= start_date + 30 && thirty == 366) {
                thirty = i;
            }
        }
        
    
        memo[start] = min(costs[0] + dp(one, days, costs), 
                         costs[1] + dp(seven, days, costs),
                         costs[2] + dp(thirty, days, costs));
        
        return memo[start];
    }
    
    public int min(int a, int b, int c) {
        
        return Math.min(a, Math.min(b, c));
        
    }
}