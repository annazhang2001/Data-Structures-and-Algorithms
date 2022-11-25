class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> track = new ArrayList<>();

        backtrack(0, nums.length, res, track, nums);

        return res;
    }

    void backtrack(int idx, int n, List<List<Integer>> res, List<Integer> track, int[] nums) {

        res.add(new ArrayList<>(track));

        for (int i = idx; i < n; i++) {
            track.add(nums[i]);
            backtrack(i+1, n, res, track, nums);
            track.remove(track.size()-1);
        }
    }
}