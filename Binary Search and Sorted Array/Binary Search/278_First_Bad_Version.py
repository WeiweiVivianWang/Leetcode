# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        start = 1
        end = n 
        while start + 1 < end:
            mid = start + (end - start) // 2
            if isBadVersion(mid) == True:
                end = mid
            else:
                start = mid
                
        if isBadVersion(start) == True:
            return start
        if isBadVersion(end) == True:
            return end
        
        
 #Time O(logn)
 #Space O(1)           
            
        