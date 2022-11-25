class Solution {
    public int trap(int[] height) {
        // Two pointers
        int n = height.length;
        int res = 0;

        int l_max = 0;
        int r_max = 0;

        int left = 0;
        int right = n - 1;

        while (left < right) {
            l_max = Math.max(height[left], l_max);
            r_max = Math.max(height[right], r_max);
            if (l_max < r_max) {
                res += l_max - height[left];
                left++;
            } else {
                res += r_max - height[right];
                right--;
            }
        }

        return res;
    }
}