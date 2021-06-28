from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k ==0: return 0
        valid = 0
        left, right = 0, 0
        dic = defaultdict(int)
        length = 0
            
        for left in range(len(s)):
            
            while valid <=k and right <len(s):
                
                char = s[right]
                dic[char]+=1
                if dic[char]==1:
                    valid +=1
                if valid <=k:
                    length = max(length, right - left +1)
                right +=1
                
            char_left = s[left]    
            dic[char_left]-=1  
            if dic[char_left]==0:
                valid -=1
                
                
        if length == 0: return ""
        
        return length
            
#Time O(N) in the best case of k distinct characters in the string and O(Nk) in the worst case of N distinct
#characters in the string
#Space: O(k) since additional space is used only for a hashmap with at most k+1 elements

            
                
                
               
                
                
                
                
          
                
            
            
        
        