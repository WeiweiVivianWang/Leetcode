class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        
        if len(nums) == 0 or nums is None: return 0
        left, right = 0,0
        su = 0
        min_length = sys.maxsize
        for right in range(len(nums)):
            su += nums[right]
            
            while su >= target:
                min_length = min(min_length, right - left+1)
                su -= nums[left]
                
                left += 1
        if min_length == sys.maxsize: return 0
        return min_length
                


#Time O(N)
#Each element can be visited atmost twice, once by the right pointer i and (at most) once by the left pointer
#Space 0(1) 
#Only constant space required for left sum ans and i

# 双指针同向男生追女生问题 女生永远在前 男生在后， 当sum <target, 女生往前走，如果sum > target, 男生往前走， 女生永不后退， max length是n+1，如果最后找到最小的还是n+1， 说明没找到。