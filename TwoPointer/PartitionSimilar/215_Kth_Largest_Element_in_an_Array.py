class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        return self.quickSelect(nums, 0, len(nums)-1, k)

    def partition(self, nums,left, right):
        i = left
        pivot = nums[right] # pick the last one as pivot
        for j in range(left, right): # left to right -1

            if nums[j] > pivot: # the larger elements are in left side

                nums[i], nums[j] = nums[j], nums[i]
                i+=1

        nums[right], nums[i] = nums[i], nums[right] # swap the i and the last element

        return i
    
    def quickSelect(self, arr, start, end, k):
        pos = self.partition(arr,start, end)

        if pos == k-1: 
            return arr[pos]

        elif pos>=k: 
            return self.quickSelect(arr, 0, pos-1, k)

        else: 
            return self.quickSelect(arr, pos+1, end, k)

# Time:O(N) is best, avg O(NlogN), O(N^2) in the worst case
# Space: O(1)

#heap

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heappush(heap, num)
            if len(heap) > k:
                heappop(heap)
        return heappop(heap)


