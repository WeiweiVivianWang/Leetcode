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
 


 class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums[0] < nums[-1]: return self.binarySearch(nums,0,len(nums)-1,target)
        if len(nums) ==0: return None
        if len(nums) == 1:
            if target != nums[0]: 
                return -1
            else:
                return 0
        
        # if len(nums)==2:
        #     return self.binarySearch(nums,0,1,target)
            
        peak_index = self.find_peak_index(nums)
        
        if nums[0] <= target <= nums[peak_index]:      
            return self.binarySearch(nums,0,peak_index,target)
        
        else:
            
            return self.binarySearch(nums,peak_index+1,len(nums)-1,target)
        
    def find_peak_index(self, nums):
        start = 0
        end = len(nums) -1
        while start + 1 < end:
            mid = start + (end - start) //2          
            if nums[mid] > nums[mid+1]: return mid
            elif nums[mid] > nums[start]:
                start = mid
            else:
                end = mid
                
        if nums[start] > nums[end]: return start
        else:
            return end
        
    def binarySearch(self,nums, start, end, target):
        # start = 0
        # end = len(nums) -1
        while start + 1 < end:
            mid = start + (end -start)//2
            if nums[mid] == target: return mid
            if nums[mid] > target:
                end = mid
            else:
                start = mid
                
        if nums[start] == target: return start 
        if nums[end] == target: return end
        return -1
        
    
                
        