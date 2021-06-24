class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) ==0: return 0

        left = 0
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]
        water = 0
        while left <= right:
            if left_max < right_max:
                left_max = max(left_max,height[left])
                water = water +left_max-height[left]
                left+=1
            else:
                right_max = max(right_max, height[right])
                water = water + right_max-height[right]
                right-=1
                
        return water

#每个位置上的盛水数目 = min(左侧最高，右侧最高) - 当前高度
# Time O(N)
# Space O(1)
                
     