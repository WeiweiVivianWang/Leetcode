class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        
        while start + 1 < end:
            mid = start + (end - start)//2
            if nums[mid] > nums[mid + 1]:
                end = mid
                
            else:
                start = mid
                
                
                
        if nums[start] > nums[end]:
            return start
        else:
            return end
# For any value in the array, it is either in an increasing subarray or a decreasing subarray.
# We can determine this by comparing this value to the value to its right. 
#If it's larger than the value to its right, then it's in a decreasing subarray, 
#and the peak element can either be itself or some element to its left. 
#If it's smaller than the value to its right, then the peak element must be some element to the right of the current element.
                
                
            
                
            
         
            