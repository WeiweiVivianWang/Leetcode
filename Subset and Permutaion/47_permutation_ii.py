class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []
        used = [0] * len(nums)
        path = []
        # 排序
        nums = sorted(nums)
        # dfs
        self.dfs(nums, used, path, res)
        return res
    
    def dfs(self, nums, used, path, res):
        if len(path) == len(nums):
            res.append(path[:])
            return
        
        for i in range(len(nums)):
            # 元素已访问过 或者 是重复元素
            if used[i] or (i > 0 and nums[i] == nums[i-1] and not used[i-1]):
                continue
            # 在路径添加该节点，递归
            used[i] = 1
            self.dfs(nums, used, path + [nums[i]], res)
            # 回溯
            used[i] = 0
            
        