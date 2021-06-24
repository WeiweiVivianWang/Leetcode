class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        #排序
        subset =[]
        #dfs搜索
        self.dfs(nums,0,subset,res)
        return res
    
    def dfs(self,nums,k,subset,res):
        #当前组合存入res
        res.append(subset[:])
        #为subset新增一位元素
        for i in range(k,len(nums)):

            #剪枝
            if (i!=k and nums[i]==nums[i-1]): continue
            subset.append(nums[i])
            #下一层搜索
            self.dfs(nums,i+1,subset,res)
            #回溯
            
            subset.pop()