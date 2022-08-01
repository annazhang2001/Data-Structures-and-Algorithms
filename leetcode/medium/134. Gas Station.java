class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        
        // Greedy
        int n = gas.length;
        int start = 0;
        int cur_tank = 0, total_tank = 0;
        
        for (int i = 0; i < n; i++) {
            total_tank += gas[i] - cost[i];
            cur_tank += gas[i] - cost[i];
            if (cur_tank < 0) {
                start = i + 1;
                cur_tank = 0;
            }
        }
        return total_tank >= 0 ? start : -1;
    }
}