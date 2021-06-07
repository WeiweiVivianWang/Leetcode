class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        results = []

        # 如果数组为空直接返回空
        if nums is None:
            return []

        # dfs
        #首先需要定义并初始化一个bool类型used数组记录每个数字是否已被使用
        used = [0] * len(nums)
        self.dfs(nums, used, [], results)
        return results

    def dfs(self, nums, used, current, results):

        # 找到一组排列，已到达边界条件
        if len(nums) == len(current):
            # 因为地址传递，在最终回溯后current为空导致results中均为空列表
            # 所以不能写成results.append(current)
            results.append(current[:])
            return

        for i in range(len(nums)):
            # i位置这个元素已经被用过
            if used[i]:
                continue

            # 继续递归
            current.append(nums[i])
            used[i] = 1
            self.dfs(nums, used, current, results)
            used[i] = 0
            current.pop()
        