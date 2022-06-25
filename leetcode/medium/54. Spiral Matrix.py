class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        
        m = len(matrix)
        n = len(matrix[0])
        
        upper_bound = 0
        left_bound = 0
        lower_bound = m - 1
        right_bound = n - 1
    
        while (len(result) < m * n):
            
            # 从左到右（顶部）
            if (upper_bound <= lower_bound):
                for i in range(left_bound, right_bound + 1):
                    result.append(matrix[upper_bound][i])
                
                # 上边界下移
                upper_bound += 1
                
            
            # 从上到下（右）
            if (left_bound <= right_bound):
                for i in range(upper_bound, lower_bound + 1):
                    result.append(matrix[i][right_bound])
                    
                # 右边界左移
                right_bound -= 1
            
            # 从右到左（底部）
            if (upper_bound <= lower_bound):
                for i in range(right_bound, left_bound - 1, -1):
                    result.append(matrix[lower_bound][i])
                    
                # 下边界上移
                lower_bound -= 1
            
            # 从下到上（左）
            if (left_bound <= right_bound):
                for i in range(lower_bound, upper_bound - 1, -1):
                    result.append(matrix[i][left_bound])
                
                # 左边界右移
                left_bound += 1
                
        return result
            
            
        