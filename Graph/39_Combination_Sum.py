class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates = sorted(list(set(candidates))) #sort, 去重
        index = 0
        current = []
        results = []
        remain_target = target
        
        self.dfs(candidates, remain_target, index, current, results)
        
        return results
    
    def dfs(self, candidates, remain_target, index, current, results):
        
        if remain_target == 0:
            return results.append(current[:])
        
        for i in range(index, len(candidates)):
            if remain_target < 0:
                break
                
            current.append(candidates[i])
            self.dfs(candidates, remain_target - candidates[i], i, current, results) # i: 因为每次当前值都可以再选择
            current.pop()
            
            
            
#Time O(n^(target/min)) n为集合中数字个数，min为集合中最小的数字, 每个位置可以取集合中的任意数字，最多有target/min个数字。
#Space O(n^(target/min)) n为集合中数字个数，min为集合中最小的数字 对于用来保存答案的列表，最多有 n^(target/min)组合
