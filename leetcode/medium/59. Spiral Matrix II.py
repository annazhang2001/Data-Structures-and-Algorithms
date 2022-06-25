class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        upper_bound = 0
        left_bound = 0
        lower_bound = n - 1
        right_bound = n - 1
        
        result = [[0 for i in range(n)] for i in range(n)]
        num = 1
    
        while (num <= n * n):
            
            # 从左到右（顶部）
            if (upper_bound <= lower_bound):
                for i in range(left_bound, right_bound + 1):
                    result[upper_bound][i] = num
                    num += 1
            
                # 上边界下移
                upper_bound += 1

                
            
            # 从上到下（右）
            if (left_bound <= right_bound):
                for i in range(upper_bound, lower_bound + 1):
                    result[i][right_bound] = num
                    num += 1
                    
                # 右边界左移
                right_bound -= 1
            
            # 从右到左（底部）
            if (upper_bound <= lower_bound):
                for i in range(right_bound, left_bound - 1, -1):
                    result[lower_bound][i] = num
                    num += 1
                
                # 下边界上移
                lower_bound -= 1
            
            # 从下到上（左）
            if (left_bound <= right_bound):
                for i in range(lower_bound, upper_bound - 1, -1):
                    result[i][left_bound] = num
                    num += 1
                
                # 左边界右移
                left_bound += 1
                
        return result
            
            
        