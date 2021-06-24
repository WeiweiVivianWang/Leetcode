#Quicksort
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        return self.quicksort(0,len(nums)-1, nums)
         
    def partition(self, left,right,array):
        i = left
        pivot = array[right]
        for j in range(left, right):
            if array[j] < pivot:
                array[j], array[i] = array[i],array[j]
                i+=1
        array[i], array[right] = array[right], array[i]
        
        return i
    
    def quicksort(self, start, end, array):
    
        if start < end:
            pos = self.partition(start,end, array)
            self.quicksort(start, pos-1, array)
            self.quicksort(pos+1, end, array)
#One Pass       
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0 = 0
        p2 = len(nums)-1
        curr = 0
        while curr <= p2:
            if nums[curr] == 0:
                nums[curr], nums[p0] = nums[p0], nums[curr]
                p0+=1
                curr+=1
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2-=1
                
            else:
                curr+=1
                
        return nums

#Time O(N), Space O(1)