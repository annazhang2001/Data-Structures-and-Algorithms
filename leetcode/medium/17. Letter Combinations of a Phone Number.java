class Solution {
    HashMap<Character, String[]> map = new HashMap<>();
    StringBuilder track = new StringBuilder();
    List<String> res = new LinkedList<>();

    public List<String> letterCombinations(String digits) {
        map.put('2', new String[]{"a", "b", "c"});
        map.put('3', new String[]{"d", "e", "f"});
        map.put('4', new String[]{"g", "h", "i"});
        map.put('5', new String[]{"j", "k", "l"});
        map.put('6', new String[]{"m", "n", "o"});
        map.put('7', new String[]{"p", "q", "r", "s"});
        map.put('8', new String[]{"t", "u", "v"});
        map.put('9', new String[]{"w", "x", "y", "z"});

        int n = digits.length();
        if (n == 0) return res;
        
        backtrack(0, n, digits);

        return res;

    }

    void backtrack(int idx, int n, String digits) {
        if (idx == n) {
            if (track.length() == n) {
                res.add(track.toString());
            }
            
            return;
        } 
        
        for (Integer i = idx; i < n; i++) {
            char c = digits.charAt(i);
            String[] lst = map.get(c);
            
            for (String a : lst) {
                track.append(a);
                backtrack(i+1, n, digits);
                track.deleteCharAt(track.length()-1);
            }
            
        }
    }
}