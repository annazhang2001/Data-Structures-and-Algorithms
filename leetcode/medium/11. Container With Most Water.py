class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        left = 0
        right = len(height) - 1
        max_area = -1
    
        while left < right:
            left_side = height[left]
            right_side = height[right]
            
            min_side = min(left_side, right_side)
            area = (right - left) * min_side
            max_area = max(area, max_area)
            
            if left_side < right_side:
                left += 1
            else:
                right -= 1
        
        return max_area
            
        