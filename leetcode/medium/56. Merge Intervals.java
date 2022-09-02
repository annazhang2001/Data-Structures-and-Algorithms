class Solution {
    public int[][] merge(int[][] intervals) {
        ArrayList<int[]> res = new ArrayList<>();
        Arrays.sort(intervals, (a, b) -> {
            
            return Integer.compare(a[0], b[0]);
        });
        
        int i = 1;
        int n = intervals.length;
        int start = intervals[0][0];
        int end = intervals[0][1];
        
        while (i <= n) {
            while (i < n && intervals[i][0] <= end) {
                end = Math.max(end, intervals[i][1]);
                i++;
            }
            
            int[] interval = new int[] {start, end};
            res.add(interval);
            
            if (i < n) {
                start = intervals[i][0];
                end = intervals[i][1];
            }
            
            i++;
        }
        
        return res.toArray(new int[res.size()][]);
        
    }
}