class Solution {
    
    public List<List<String>> groupAnagrams(String[] strs) {
    
        HashMap<String, List<String>> map = new HashMap<>();
        for (String s : strs) {
            String enc = encode(s);
            map.putIfAbsent(enc, new LinkedList<>());
            map.get(enc).add(s);
        }
        
        List<List<String>> res = new LinkedList<>();
        for (List<String> list : map.values()) {
            res.add(list);
        }
        
        return res;
        
    }
    
    String encode(String s) {
        char[] count = new char[26];
        for (char c : s.toCharArray()) {
            int delta = c - 'a';
            count[delta]++;
        }
        return new String(count);
    }
    
}