class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        p1 = m-1
        p2 = n-1
        end = m+n-1
        while 0<=p1<=m-1 and 0<=p2<=n-1:# 从后往前一对一对比较
            if nums1[p1]>=nums2[p2]:
                nums1[end]=nums1[p1]
                p1-=1
                end-=1
            else:
                nums1[end]=nums2[p2]
                p2-=1
                end-=1
                
        while 0<=p1<=m-1:
            nums1[end]=nums1[p1]
            p1-=1
            end-=1
            
            
        while 0<=p2<=n-1:
            nums1[end]=nums2[p2]
            p2-=1
            end-=1
            
        return nums1
 #第一种方法inplace 改变nums1
 #Time O(m+n)
 #Space O(1)       


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


#Time O(n+m)
#Space O(n+m)