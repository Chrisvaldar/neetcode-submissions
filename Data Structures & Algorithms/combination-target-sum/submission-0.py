class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        curr_comb = []
        res = []

        def dfs(i):
            if sum(curr_comb) == target:
                res.append(curr_comb.copy())
                return
            elif sum(curr_comb) > target or i >= len(nums):
                return

            curr_comb.append(nums[i])
            dfs(i)
            curr_comb.pop()
            dfs(i + 1)
        dfs(0)
        return res