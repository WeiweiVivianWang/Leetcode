class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums)==0: return []
        

        current = []
        result = []
        visited = set()
        self.dfs(nums, visited, current, result)#输入数组 去重工具 中间结果 最终结果
        return result
    
    
    def dfs(self, nums, visited, current, result):
        if len(current) ==len(nums):
            # result.append(list(current)) #此处用list
            result.append(current[:])
            return
        for i in nums:
            if i in visited:
                continue
                
            current.append(i)
            visited.add(i)
            self.dfs(nums,visited,current,result)
            visited.remove(i)
            current.pop()
    
        