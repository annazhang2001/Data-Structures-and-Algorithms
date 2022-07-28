package leetcode.easy;

class Solution {
    public boolean canAttendMeetings(int[][] intervals) {
        if (intervals.length == 0) {
            return true;
        }
        Arrays.sort(intervals, (a, b) -> {
            return Integer.compare(a[1], b[1]);
        });
        int end = intervals[0][1];
        
        for (int i = 1; i < intervals.length; i++) {
            int start = intervals[i][0];
            if (start < end) {
                return false;
            }
            end = intervals[i][1];
        }
        
        return true;
    }
    
}
