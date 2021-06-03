#167. Two Sum II - Input array is sorted
# Given an array of integers numbers that is already sorted in non-decreasing order, 
#find two numbers such that they add up to a specific target number.

# Return the indices of the two numbers (1-indexed) as an integer array answer of size 2,
# where 1 <= answer[0] < answer[1] <= numbers.length.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        dict = {}
        for i in range(len(numbers)):
            if target - numbers[i] in dict:
                return [dict[target - numbers[i]]+1,i+1] #注意 有顺序
            dict[numbers[i]] = i # 注意 key是数值， value 是index
