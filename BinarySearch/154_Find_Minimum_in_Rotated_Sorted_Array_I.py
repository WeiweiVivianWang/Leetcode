class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums[0] < nums[-1]: return nums[0] 
        if len(nums)==1: return nums[0]
        
        start, end = 0, len(nums) -1
        while start + 1 < end:
            mid = start + (end - start) //2
            if nums[mid] < nums[mid -1]: return nums[mid]
            if nums[mid] < nums[end]: 
                end = mid
            elif nums[mid] > nums[end]:
                start = mid
            elif nums[mid] == nums[end]:#多加这一步 [10,1,10,10,10]／[10,10,10,1,10] 无法判断最小值的位置
                end -=1
                
        if nums[start]<= nums[end]: return nums[start]
        if nums[end] < nums[start]: return nums[end]
        
        return -1
        