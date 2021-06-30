class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        mid = 0
        
        while start + 1 < end:
            mid = start + (end - start) //2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid
            else:
                end = mid
                
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1
#Given an array of integers nums which is sorted in ascending order, and an integer target, 
#write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
#all entry in the array are unique

#最基础的binary search 此为模版 ---最终会得到一个start 一个end

#Time O(logN)
#Space O(1)


#If have duplicates and return the first occurance position of the target
 #same code
 # If return last occurance position of the target, code is :
   
    # if nums[end] == target:
    #         return end
    # if nums[start] == target:
    #         return start
