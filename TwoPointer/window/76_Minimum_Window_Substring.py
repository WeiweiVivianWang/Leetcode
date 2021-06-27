from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        start = -1
        left, right = 0, 0
        min_len = sys.maxsize
        valid =0
# 初始 counter source和counter target，把target放入dict里面，此dict永远不变，作为参照组       
        counter_s = defaultdict(int)
        counter_t = defaultdict(int)
        
        for char in t:
            counter_t[char] +=1
            
        for right in range(len(s)):
            ch = s[right]
            if ch in counter_t:
                counter_s[ch] +=1
                
                if counter_s[ch] ==counter_t[ch]:
                    valid +=1
                    
            while valid ==len(counter_t):# 用while不是if 当找到符合的valid时，收缩left直到找到length最短
                if right - left + 1 < min_len:
                    
                    min_len = right - left + 1
                    start = left #记录当前最短的start位置方便之后返回整个array
                
                left_char = s[left]
                left +=1
                
                if left_char in counter_s:
                    counter_s[left_char] -= 1
                    #只有source里面的counter少于target才减少valid （如果target里面有一个A， source里面有两个A，减少了一个A还是符合valid的， 这种情况valid不减少
                    if counter_s[left_char] < counter_t[left_char]:
                        valid -=1
                    
        if min_len == sys.maxsize: return ""
            
        return s[start:start+min_len]


#Time: O(|S|+|T|) where |S|,|T| represent the lengths of string S and T.
# Worst case we might end up visiting every elenents of string S twice, once by left and once by right pointer
#Space O(|S|+|T|). |S| when the window size is equal to the entire string S. |T| when T has all unique characters.        
                
            
        
        
        
        
        
        