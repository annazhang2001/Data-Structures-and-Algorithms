class Solution {
    public long minimumHealth(int[] damage, int armor) {
        long sum = 0;
        for (int i : damage) {
            sum += i;
        }
        sum += 1;
        long res = sum;
        int n = damage.length;
        
        for (int i = 0; i < n; i++) {
            res = Math.min(res, sum - Math.min(damage[i], armor));
        }
        
        return res;
    }
}