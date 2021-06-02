#Q. Given an array of integers nums and an integer k, 
#return the total number of continuous subarrays whose sum equals to k.

#1. Brute force i, j 指针代表。subarray开始和结束的位置O(n^2),对于每一对i，j，求subarray之和O(n)
#Time:O(n^3), Space: O(n)

#2. step a. iteration 一遍得到cumulative summation --O(n)
#	step b. 对于所有i，j--O(n^2), 直接得到i,j之间的summation
# Time O(n^2) Space O(n)
class Solution1:
    def subarraySum(self, nums: List[int], k: int) -> int:
    	'''
    	nums = 1,2,3,2,1
    	cusums = 1,3,6,8,9
    	for any i = 1, j = 3
    	'''

    	cusum = [0] * len(nums)
    	cusum[0] = nums[0]
    	for i in range(1,len(nums)):
    		cusum[i] = cusum[i-1] + nums[i]    #cusum 模版 记住！

    	cnt = 0

    	for i in range(len(nums)):
    		for j in range(i, len(nums)):

    			sum_ij= cusum[j]-cusum[i]+nums[i]
    			if sum_ij ==k:
    				cnt +=1


    	return cnt
#3. Hashmap (key: summation, values: number of occuarrance)
#一遍iteration，在每一个元素计算当前元素及之前的所有的元素的和， 从hashmap
#中寻找累加。
#Time O(n) Space O(n)
class Solution2:
    def subarraySum(self, nums: List[int], k: int) -> int:
    	'''
    	[3,2,-1,1,5] ,k = 5
    	[3,5,4,5,10] 
    	{0:1,3:1,5:2,10:1}

    	'''

    	hashmap = collection.defaultdict(int)
    	hashmap[0] = 1
    	cusum = 0
    	for i in range(len(nums)):
    		cusum = cusum + nums[i]


    		if cusum - k in hashmap:
    			cnt += hashmap[cumsum - k]

    		hashmap[cusum]+=1








