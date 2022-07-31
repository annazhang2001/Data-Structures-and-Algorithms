class Solution {
    public int videoStitching(int[][] clips, int time) {
        if (time == 0) {
            return 0;
        }
        
        Arrays.sort(clips, (a, b) -> {
            if (a[0] == b[0]) {
                return Integer.compare(b[1], a[1]);
            }
            return Integer.compare(a[0], b[0]);
        });
        
        if (clips[0][0] > 0) {
            return -1;
        }
        
        int i = 0, n = clips.length;
        int curEnd = 0;
        int count = 0;
        int newEnd = 0;
        
        while (i < n && clips[i][0] <= curEnd) {
            
            while (i < n && clips[i][0] <= curEnd) {
                newEnd = Math.max(newEnd, clips[i][1]);
                i++;
            }
            
            count++;
            curEnd = newEnd;
            
            if (curEnd >= time) {
                return count;
            }
        }
        
        return -1;
    }
}