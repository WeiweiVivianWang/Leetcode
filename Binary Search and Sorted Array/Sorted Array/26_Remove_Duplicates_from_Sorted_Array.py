class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 0
        for i in range(1,len(nums)):
            if nums[i]!=nums[index]:
                index +=1
                nums[index] = nums[i]
                
        return index +1
                
                
                
#Time O(N)
#Space O(1)         
            
        