class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) ==1: return 0
        if len(height) ==0: return []
        if len(height) ==2: return min(height[0],height[1])
        area = 0
        l = 0
        r = len(height)-1
        while l < r:
            area = max(area,min(height[l] , height[r])*(r-l))
            if height[l] <= height[r]:
                l+=1
            else:
                r-=1
                
        return area
    
