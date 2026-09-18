class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # curr_comb = []
        # res = []

        # def dfs(i):
        #     if sum(curr_comb) == target:
        #         res.append(curr_comb.copy())
        #         return
        #     elif sum(curr_comb) > target or i >= len(candidates):
        #         return
            
        #     curr_comb.append(candidates[i])
        #     dfs(i + 1)
        #     curr_comb.pop()
        #     j = i + 1
        #     while j < len(candidates) and candidates[i] == candidates[j]:
        #         j += 1
        #     dfs(j)
        # dfs(0)
        # return res

        res = []
        candidates.sort()

        def dfs(idx, path, cur):
            if cur == target:
                res.append(path.copy())
                return
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                if cur + candidates[i] > target:
                    break

                path.append(candidates[i])
                dfs(i + 1, path, cur + candidates[i])
                path.pop()

        dfs(0, [], 0)
        return res