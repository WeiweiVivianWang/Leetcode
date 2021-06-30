class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) #m number of rows
        n = len(matrix[0]) #n number of columns
        
        start = 0
        end = m * n - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            element = matrix[mid//n][mid%n] #注意subset matrix里面一个element的写法
            
            if element == target: return True
            
            elif element < target:
                start = mid
            else:
                end = mid
                
        
        if matrix[start//n][start%n] == target:
            return True
        if matrix[end//n][end%n] == target:
            return True
        return False


#此题 把matrix想成铺成一个长 sorted array
#需注意index matrix 中一个 element 的写法
# element = matrix[mid//n][mid%n]
# Time O(log(m*n))
# Space O(1)