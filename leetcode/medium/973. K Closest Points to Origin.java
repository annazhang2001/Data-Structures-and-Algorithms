class Solution {
    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<Point> queue = new PriorityQueue<Point>(new PointComparator());
        for (int i = 0; i < points.length; i++) {
            int x = points[i][0];
            int y = points[i][1];
            Point pt = new Point(x, y);
            queue.add(pt);
        }
        
        int[][] res = new int[k][2];
        for (int i = 0; i < k; i++) {
            Point pt = queue.poll();
            res[i][0] = pt.x;
            res[i][1] = pt.y;
        }
        
        return res;
    }
    
    private class Point {
        int x;
        int y;
        
        double distance;
        
        Point(int x, int y) {
            this.x = x;
            this.y = y;
            this.distance = Math.sqrt(x*x + y*y);
        }
        
    }
    
    class PointComparator implements Comparator<Point> {
        public int compare(Point p1, Point p2) {
            return Double.compare(p1.distance, p2.distance);
        }
    }
}