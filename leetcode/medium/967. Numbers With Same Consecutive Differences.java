class Solution {
    public int[] numsSameConsecDiff(int n, int k) {
        ArrayList<Integer> res = new ArrayList<>();
        for (int i = 1; i <= 9; i++) {
            backtrack(n, k, 0, i, res, i);
        }
        int size = res.size();
        int[] re = new int[res.size()];
        for (int i = 0; i < size; i++) {
            re[i] = res.get(i);
        }
        return re;
    }

    void backtrack(int n, int k, int cur, int prev, ArrayList<Integer> res, int sum) {
        // Base case
        if (cur == n-1) {
            res.add(sum);
            return;
        }
        int prev_inc = prev + k;
        if (prev_inc <= 9 && prev_inc >= 0) {
            int new_sum = sum * 10 + prev_inc;
            backtrack(n, k, cur + 1, prev_inc, res, new_sum);
        } 
        if (prev - k != prev_inc) {
            int prev_dec = prev - k;
            if (prev_dec <= 9 && prev_dec >= 0) {
                int new_sum = sum * 10 + prev_dec;
                backtrack(n, k, cur + 1, prev_dec, res, new_sum);
            }
        }
    }
}