class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #排序
        nums.sort()
        res = []
        subset = []
        #dfs搜索
        self.dfs(nums,0,subset, res)
        return res
        
    def dfs(self,nums,k,subset,res):
        #当前组合存入res
        res.append(subset[:]) #The [:] makes a shallow copy of the array, hence  when you modify memory (subset), won't affect copy.
        # print('...',res)
        #为subset新增一位元素
        for i in range(k,len(nums)):
            subset.append(nums[i])
            #下一层搜索
            
            self.dfs(nums,i+1,subset,res)
            #回溯
            del subset[-1]


#backtracking + dfs
#backtracking 画树
# []

# [1],[1,2],[1,2,3]
# [1,3]

# [2]
# [2,3]

# [3]
# 时间复杂度：O(n * 2 ^ n)其中n为nums的长度。生成所有子集，并复制到输出集合中。
# 空间复杂度：O(n * 2 ^ n)其中n为nums的长度。存储所有子集，共 n个元素，每个元素都有可能存在或者不存在。