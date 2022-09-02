class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        
        int n = intervals.length;
        LinkedList<int[]> res = new LinkedList<>();
        int i = 0;
        int newStart = newInterval[0], newEnd = newInterval[1];
        
        while (i < n && newStart > intervals[i][0]) {
            res.add(intervals[i]);
            i++;
        }
        
        // no overlap (front)
        if (res.isEmpty() || newStart > res.getLast()[1]) {
            res.add(newInterval);
        } else {
            res.getLast()[1] = Math.max(res.getLast()[1], newEnd);
        }
        
        while (i < n) {
        
            int[] interval = intervals[i];
            
            // no overlap (front)
            if (interval[0] > res.getLast()[1]) {
                res.add(interval);
            } else {
                res.getLast()[1] = Math.max(interval[1], res.getLast()[1]);
            }
            
            i++;
            
        }
        
        return res.toArray(new int[res.size()][2]);
        
        
    }
}