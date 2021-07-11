class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda x: x[0])
        print(intervals)
        result = []
        for i in intervals:
            if result ==[] or result[-1][1]<i[0]:
                result.append(i)
            else:
                result[-1][1] = max(i[1], result[-1][1])#[1,4],[2,3]/[1,3],[2,4]
                
        return result

#排序的时间复杂度为O(NlogN)。
# 遍历一遍数组的时间复杂度为O(N)。
# 总时间复杂度为O(NlogN)
#空间复杂度为O(n)，可能存在每一个区间都不与任何一段区间相交，返回的答案和传入的参数长度相等。