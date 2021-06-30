class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        
        i = row - 1
        j = 0
        
        # count = 0
        
        while i >= 0 and j < col:
            
            if matrix[i][j] == target: return True
                #count +=1
                # i-=1
                # j+=1
            elif matrix[i][j] < target:
                j += 1
            else:
                i -=1
        # if count>=0: return True
        
        return False
                
# We initialize a (row, col) pointer to the bottom left of the matrix. 
# if currently pointer is larger than target, we move one row up, 
# if smaller, move one column right
#Time O(n+m)
#on every iteration (during which we do not return true) either row or col is is decremented/incremented exactly once. Because row can only be decremented 
#m times and col can only be incremented 
#n times before causing the while loop to terminate, the loop cannot run for more than n+m iterations. 
#Because all other work is constant, the overall time complexity is linear in the sum of the dimensions of the matrix.
#Space O(1)



