class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums)==0: return []
        nums = sorted(nums)
        result = []
        index = 0
        current = []
        self.dfs(nums,index,current,result)
        return result
        
    def dfs(self,nums,index,current,result):
        result.append(current[:])
        for i in range(index,len(nums)):
            current.append(nums[i])
            self.dfs(nums,i+1,current,result)
            current.pop()

