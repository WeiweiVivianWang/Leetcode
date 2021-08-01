class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        index = 0
        current = []
        result = []
        self.dfs(nums, index, current, result)
        return result
    
    def dfs(self, nums, index, current, result):
        result.append(current[:])
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            current.append(nums[i])
            self.dfs(nums, i+1, current, result)
            current.pop()

        