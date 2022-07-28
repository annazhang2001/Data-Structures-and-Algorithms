class Solution {
    public int findMinArrowShots(int[][] points) {
        return intervalScheduling(points);
    }
    
    public int intervalScheduling(int[][] intervals) {
        if (intervals.length == 0) {
            return 0;
        }
        
       Arrays.sort(intervals, (a, b) -> {
            return Integer.compare(a[1], b[1]);
        });
        
        int end = intervals[0][1];
        int count = 1;
        for (int[] interval : intervals) {
            int start = interval[0];
            if (start > end) {
                count++;
                end = interval[1];
            }
        }
        
        return count;
    }
}