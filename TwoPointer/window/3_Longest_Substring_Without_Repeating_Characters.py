class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        longest = 0
        char = set()
        for left in range(len(s)):
            while right < len(s) and s[right] not in char:
                char.add(s[right])
                longest = max(longest, right - left + 1)
                right +=1
            char.remove(s[left])
            
        return longest
#前向性指针           
#Time 0(N)
#Space O(min(m,n))--hashmap
#space O(m)--m is the size of charset