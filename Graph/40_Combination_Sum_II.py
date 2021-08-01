class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        index = 0
        remain_target = target
        results = []
        current = []
        
        self.dfs(candidates, remain_target, index, current, results)
        
        return results
    
    def dfs(self, candidates, remain_target, index, current, results):
        if remain_target ==0:
            return results.append(current[:])
        for i in range(index, len(candidates)):
            if remain_target < 0: break
                
            if i > index and candidates[i]==candidates[i-1]:
                continue
                
            current.append(candidates[i])
            self.dfs(candidates, remain_target-candidates[i], i+1, current, results)
            current.pop()
            