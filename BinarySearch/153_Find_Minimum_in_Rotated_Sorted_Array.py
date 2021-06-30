class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        

        if nums[0] < nums[-1]: return nums[0]
        start, end = 0, len(nums)-1
        while start + 1 < end:
            mid = start + (end - start)//2
            if nums[mid] < nums[mid-1]: return nums[mid]
            
            if nums[mid] > nums[end]:
                
                start = mid
            else:
                end = mid
                
        return min(nums[start],nums[end])
            
#Time O(logN)
#Space O(1)        