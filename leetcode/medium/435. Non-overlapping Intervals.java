class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        return (intervals.length - intervalSchedule(intervals));
        
    }
    
    public int intervalSchedule(int[][] intervals) {
        if (intervals.length == 0) {
            return 0;
        }
        Arrays.sort(intervals, new Comparator<int[]>() {
            public int compare(int[] a, int[] b) {
                return a[1] - b[1];
            }
        });
        
        int end = intervals[0][1];
        int count = 1;
        
        for (int[] interval : intervals) {
            int start = interval[0];
            if (start >= end) {
                count++;
                end = interval[1];
            }
        }
        
        return count;
        
    }
}
