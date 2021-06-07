# Description
# For a given source string and a target string, you should output the first index(from 0) of target 
#string in the source string.If the target does not exist in source, just return -1.

class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """
    def strStr(self, source, target):
        # Write your code here

        if source is None or target is None : return -1
        if len(source)<len(target): return -1
        for i in range(0,(len(source)-len(target)+1)):
            if source[i:i+len(target)]==target:
                return i
            else: continue
        return -1

 #O((source_len - target_len )target_len )
        

