class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # if s is None or len(s) == 0: return []
        if len(s)>=13: return []
        index = 0
        subset = []
        result = []
        self.dfs(s,index,subset,result)
        return result
        
    def dfs(self, s, index, subset, result):
        if len(subset) == 4 and index == len(s):
            result.append('.'.join(subset))
            return
        else:
            print("...")      
        for i in range(index, index + 3):
            if i >= len(s):
                return
                # or break
            substring = s[index : i + 1]
            num = int(substring)
            # if num < 0 or num > 255 or len(substring) != len(str(num)): continue
            #  一个解决255，一个解决leading 0 的问题
            if num > 255 or len(substring) != len(str(num)): continue
                
            subset.append(substring)
            self.dfs(s, i+1, subset, result)
            subset.pop()