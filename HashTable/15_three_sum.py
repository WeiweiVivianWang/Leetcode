# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
#such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Example 2:

# Input: nums = []
# Output: []
# Example 3:

# Input: nums = [0]
# Output: []

#方法一：
# sort方便deduplicate，two sum 返回数值（not index），set（）用来dedup，a+b+c = 0 => -a = b+c 
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() #sort 后方便之后deduplicate, 可以跳过，但是不会优化程序，sort--O(nlogn) < 程序 O(n^2)
        
        def twoSum(nums:List[int],target):
            """
            find list of unique tuples, such that the summation in each tuple is                equal to target
            """  
            res = set()
            hashset = set()
            for num in nums:
                if target -  num in hashset:
                    res.add((target - num, num))
                hashset.add(num)
            return res
            
        if len(nums) < 3: return []
        
        res = set()
        # res = [] 
        for idx in range(len(nums)-2):
            a = nums[idx]
            nums_remaining = nums[idx+1:]
            target_remaining = 0 - a
            
            for b, c in twoSum(nums_remaining, target_remaining):
                res.add((a,b,c))
                # res.append([a,b,c])
                
        return res
        #return set(res)
        
# sort first 避免重复
# two sum用set---（set就是hashset，只存value，没有key）而不是dict,因为返回的是数值不是index

# set.add() 而不是append()因为 不能set(list of list) , set 存结果可以保证结果是unique的
# Time O(n^2) Space O(1) 或者 O（n)-> space required for storing sorted array

#方法二 two pointer
#how to avoid duplicates
#a: if found a equals to previous number,skip [-4,-1,-1,0,1,3] a = first -1, [0,1]=> [-1,0,1]
# b,c [-4,-1,-1,-1,-1,-1,5] skip
# Time O(n^2)
# Space O(1) 或者 O（n)-> space required for storing sorted array
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3: return []
        nums.sort()
        """
        idx,jdx,kdx represent the index of the three numbers, also idx<jdx<kdx
        """
        
        idx = 0
        res = []
        while idx<len(nums) - 2:
            if idx > 0 and nums[idx] == nums[idx-1]: #每到一位跟前一位比较，如相同则跳过
                idx +=1
         
                continue # continue 跳过此轮 进入下一轮 
            
            jdx = idx +1
            kdx = len(nums)-1
            
            while jdx < kdx:
                s = nums[idx] + nums[jdx] + nums[kdx]
                if s == 0:
                    res.append([nums[idx], nums[jdx], nums[kdx]])
                    
                    while jdx < kdx and nums[jdx] == nums[jdx +1]:#不能用if 
                        jdx += 1
                    
                    while jdx < kdx and nums[kdx] == nums[kdx -1]:
                         kdx -= 1
                        
                        
                    jdx += 1
                    kdx -= 1
                    
                elif s< 0:
                    jdx +=1
                else:
                    kdx -=1
            idx +=1
        return res
                    
                    
                    
            
            