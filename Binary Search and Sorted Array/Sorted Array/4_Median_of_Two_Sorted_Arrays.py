class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        res = []
        i = j = 0
        l1 = len(nums1)
        l2 = len(nums2)
        l = l1 + l2
        
        while i<l1 and j<l2:
            if nums1[i]<nums2[j]:
                res.append(nums1[i])
                i+=1
            else:
                res.append(nums2[j])
                j+=1
        while i<l1:
            res.append(nums1[i])
            i+=1
            
        while j<l2:
            res.append(nums2[j])
            j+=1
            
        if l%2==0:
            return (res[l//2]+res[l//2-1])/2.0
        else:
            return res[l//2]
#Time O(m+n)
#Space O(m+n)

class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        m, n = len(A), len(B)
        # 如果是奇数
        if (m + n) % 2 == 1:
            return self.getKth(A, 0, len(A) - 1, B, 0, len(B) - 1, (m + n) // 2  + 1)
        # 如果是偶数
        left = self.getKth(A, 0, len(A) - 1, B, 0, len(B) - 1, (m + n) // 2)
        right = self.getKth(A, 0, len(A) - 1, B, 0, len(B) - 1, (m + n) // 2 + 1)
        return (left + right) / 2

    def getKth(self, A, start1, end1, B, start2, end2, k):
        len1 = end1 - start1 + 1
        len2 = end2 - start2 + 1
        # 让 len1 的长度小于 len2，这样就能保证如果有数组空了，一定是 len1 
        if (len1 > len2): 
            return self.getKth(B, start2, end2, A, start1, end1, k)
        # A数组排除完毕
        if (len1 == 0):
            return B[start2 + k - 1]
        # 已经找到第k小的数
        if k == 1:
            return min(A[start1], B[start2])
        # 开始二分
        i = start1 + min(len1, k // 2) - 1
        j = start2 + min(len2, k // 2) - 1
        if (A[i] > B[j]):
            return self.getKth(A, start1, end1, B, j + 1, end2, k - (j - start2 + 1))
        else:
            return self.getKth(A, i + 1, end1, B, start2, end2, k - (i - start1 + 1))           


#Time O(log(m+n))
#Space O(1)

#建立辅助函数getKth，参数有数组A，A的起始指针start1和终止指针end1, 相对应的有B、start2和end2，以及整数k，
#目标是找到A[start1:end1]和B[start2:end2]中第k小的元素。
#在主程序中，看m + n的奇偶性，并调用getKth函数。如果是奇数，返回数组A和B的第(m + n) // 2 + 1小元素；如果是偶数，返回数组A和B的第(m + n) // 2小和第(m + n) // 2 + 1小元素的均值。            
#getKth(nums1, start1, end1, nums2, start2, end2, k)函数的实现方法： 
#如果有数组在[start:end]范围内为空，说明该数组已经排除完毕，第k小的元素一定存在于另一数组中，计算好索引位置返回即可。 
#如果k为1，说明已经找到第k小的数，那就是A[start1]和B[start2]中的较小值，直接返回即可。 
#定义指针i和j，分别指向A和B，使得A[start1:i]和B[start2:j]的长度分别为k // 2，通过比较A[i]和B[j]的大小，我们就可以确定排除哪段元素。 
#如果A[i] > B[j]，说明B[start2:j]不可能为第k小元素。我们对A[start1:end1]和B[j + 1:end2]继续送入getKth进行递归，
#k应该更新为k - (j - start2 + 1)。 
#* 反之，说明A[start1:i]不可能为第k小元素。
#我们对A[i + 1:end1]和B[start2:end2]继续送入getKth进行递归，k应该更新为k - (i - start1 + 1)。
