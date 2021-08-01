class Solution:
 
    def partition(self, s):
        result = []
        if len(s) == 0 or s is None:
            return result
        index = 0
        path = []
        self.dfs(s,index,path,result)
        return result
    
    def dfs(self, s, index, path, result):
        if index == len(s):
            result.append(path[:])
            return
        for i in range(index, len(s)):
            substr = s[index:i+1]
            if not self.isPalindrome(substr):
                continue
            path.append(substr)
            self.dfs(s,i+1,path,result) #因为之前是i结束，下一层从i+1开始检查字符串
            path.pop()
        
    def isPalindrome(self, s):
        start = 0
        end = len(s) - 1 
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1 
            end -= 1
        return True