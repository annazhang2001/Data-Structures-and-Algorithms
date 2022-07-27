package leetcode.medium;

class Solution {
    HashMap<Integer, Integer> map = new HashMap<>();

    public int integerBreak(int n) {
        map.put(1, 1);

        // dp solution
        for (int num = 2; num <= n; num++) {
            int res = 0;
            if (num != n) {
                res = num;
            }
            for (int i = 1; i < num; i++) {
                int val = map.get(i) * map.get(num-i);
                res = Math.max(res, val);
            }
            map.put(num, res);
        }
        
        return map.get(n);
        
    }
    
    
}