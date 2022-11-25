class Solution {
    public List<List<Integer>> combine(int n, int k) {
        LinkedList<Integer> track = new LinkedList<>();
        List<List<Integer>> res = new LinkedList<>();
        backtrack(0, 1, n, k, track, res);
        return res;
    }

    void backtrack(int idx, int start, int end, int num, LinkedList<Integer> track, List<List<Integer>> res) {
        if (idx == num) {
            res.add(new LinkedList<>(track));
            return;
        }
        for (int i = start; i <= end; i++) {
            track.addLast(i);
            backtrack(idx+1, i+1, end, num, track, res);
            track.removeLast();
        }

    }
}