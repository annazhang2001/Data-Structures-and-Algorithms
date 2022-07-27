package leetcode.medium;

class Solution {
    HashMap<Integer, Integer> map = new HashMap<>();
    int target;
    
    public int integerBreak(int n) {
        map.put(1, 1);
        target = n;
        
        // Recursive solution
        return dfs(n);
        
    }
    
    public int dfs(int n) {
        if (map.containsKey(n)) {
            return map.get(n);
        }
        
        if (n == target) {
            map.put(n, 0);
        } else {
            map.put(n, n);
        }
        
        int res = map.get(n);
        
        for (int i = 1; i < n; i++) {
            int val = dfs(i) * dfs(n-i);
            res = Math.max(res, val);
        }
        
        map.put(n, res);
        return res;
    }
    
    
}