class Solution {
    public List<String> generateParenthesis(int n) {
        StringBuilder track = new StringBuilder();
        List<String> res = new ArrayList<>();
        backtrack(n, n, track, res);
        return res;
    }
    
    void backtrack(int left, int right,
    StringBuilder track, List<String> res) {
        // Base case
        
        if (right < left) {
            return;
        } else if (right < 0 || left < 0) {
            return;
        } else if (right == 0 && left == 0) {
            res.add(track.toString());
            return;
        }

        // Recursive steps
        track.append('(');
        backtrack(left-1, right, track, res);
        track.deleteCharAt(track.length()-1);

        track.append(')');
        backtrack(left, right-1, track, res);
        track.deleteCharAt(track.length()-1);

    }
}