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
        
