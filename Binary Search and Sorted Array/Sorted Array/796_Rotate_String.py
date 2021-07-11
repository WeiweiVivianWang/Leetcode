class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if len(s)!=len(goal): return False
        ss = s *2
        if goal in ss:
            return True
        return False


#Time O(N)???
#Space O(N)