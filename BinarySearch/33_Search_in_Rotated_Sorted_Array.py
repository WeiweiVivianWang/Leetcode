class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        start , end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) //2
            if nums[mid] == target: return mid
            #此时left和mid肯定处在同一个递增数组上
                #那么就直接运用原始的二分查找
            if nums[mid] > nums[start]:
                if nums[start] <= target and target < nums[mid]: #单调
                    end = mid
                else:
                    start = mid
            else:
                #此时mid处于第二个递增数组 left处于第一个递增数组 自然的mid和right肯定处于第二个递增数组上               
                #还是直接运用原始的二分查找思想
                if target > nums[mid] and target <= nums[end]: #单调
                    start = mid
                else:
                    end = mid
                    
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1
                