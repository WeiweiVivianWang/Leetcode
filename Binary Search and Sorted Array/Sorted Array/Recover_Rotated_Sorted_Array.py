class Solution:
    """
    @param nums: An integer array
    @return: nothing
    """
    def recoverRotatedSortedArray(self, nums):
        # write your code here
        split_position = self.find_split(nums)
        if split_position == len(nums)-1:
            return 
        
        self.swap(nums, 0, split_position)
        self.swap(nums, split_position, len(nums))
        
        nums.reverse()
        return 
        
    def find_split(self, nums):
        # DO NOT use binary search!
        # Binary Search does not work on this prob
        if nums is None or len(nums) < 2:
            return 0
        
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                return i 
        # return i = len()-1 if it's already a sorted array 
        return i 
            
    def swap(self, nums, start, end):
        if start == end:
            return nums 
        
        left, right = start, end -1  
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1 
            right -= 1