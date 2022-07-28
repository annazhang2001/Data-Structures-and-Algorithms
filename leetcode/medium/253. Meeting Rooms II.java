class Solution {
    public int minMeetingRooms(int[][] intervals) {
        
        int n = intervals.length;
        int[] begin = new int[n];
        int[] end = new int[n];
        for (int i = 0; i < n; i++) {
            begin[i] = intervals[i][0];
            end[i] = intervals[i][1];
        }
        Arrays.sort(begin);
        Arrays.sort(end);
        
        int count = 0;
        int res = 0;
        int i = 0, j = 0;
        
        while (i < n && j < n) {
            if (begin[i] < end[j]) {
                i++;
                count++;
            } else {
                j++;
                count--;
            }
            res = Math.max(count, res);
        }
        
        return res;
        
    }
}
