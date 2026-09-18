class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        curr_comb = []
        res = []
        candidates.sort()

        def dfs(i):
            if sum(curr_comb) == target:
                res.append(curr_comb.copy())
                return
            elif sum(curr_comb) > target or i >= len(candidates):
                return
            
            curr_comb.append(candidates[i])
            dfs(i + 1)
            curr_comb.pop()
            j = i + 1
            while j < len(candidates) and candidates[j] == candidates[i]:
                j += 1
            dfs(j)
        dfs(0)
        return res