class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """        
        res = []       
        i,j = 0, 0
        
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                res.append(nums1[i])
                i+=1
                
            else:
                res.append(nums2[j])
                j+=1
                
        while i < m:
            res.append(nums1[i])
            i+=1
        while j < n:
            res.append(nums2[j])
            j+=1
            
        for index in range(m+n):
            nums1[index]=res[index]
       
            
#此题是改一个数组，Do not return anything, modify nums1 in-place instead.
#Time O(m+n)
#Space O(m+n) for storing res.
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # Set p1 and p2 to point to the end of their respective arrays.
        p1 = m - 1
        p2 = n - 1
    
        # And move p backwards through the array, each time writing
        # the smallest value pointed at by p1 or p2.
        for p in range(n + m - 1, -1, -1):
            if p2 < 0:
                break
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1

#Time O(m+n)
#Space O(1)
#三个pointer start from the end #!!!从大开始比较， 从后往前append！！！！
#set p1 to point at index m - 1 of nums1, p2 to point at index n - 1 of nums2, 
#and p to point at index m + n - 1 of nums1. 
#This way, it is guaranteed that once we start overwriting the first m values in nums1, 
#we will have already written each into its new position. In this way, we can eliminate the additional space.
