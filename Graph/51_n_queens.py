class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        visited = {
            'col' : set(),
            'sum' : set(),
            'diff' : set()  
        }
        
        current = []
        
        self.dfs(n, visited, current, result)
        return result
    
    def dfs(self, n, visited, current, result):
        if len(current) == n:
            result.append(self.draw(current))
            return
        row = len(current)
        for col in range(n):
            if not self.is_valid(current, visited, col):
                continue
                
            current.append(col)
            visited['col'].add(col)
            visited['sum'].add(row + col)
            visited['diff'].add(row - col)
            self.dfs(n, visited, current, result)
            visited['col'].remove(col)
            visited['sum'].remove(row + col)
            visited['diff'].remove(row - col)
            current.pop()
                
        
                
    def is_valid(self, current, visited, col):
        row = len(current)
        if col in visited['col']:
            return False
        if row + col in visited['sum']:
            return False
        if row - col in visited['diff']:
            return False
        return True
            
        
    def draw(self, current):
        result = []
        n = len(current)
        for col in current:
            row_string = ''.join(['Q' if c == col else '.' for c in range(n)])
            result.append(row_string) 
            
        return result
    
        
#dfs---permutation类似      
        
        