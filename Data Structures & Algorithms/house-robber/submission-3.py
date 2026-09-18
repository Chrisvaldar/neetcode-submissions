class Solution:
    def rob(self, nums: List[int]) -> int:
        count = dict()
        def dfs(idx):
            if idx >= len(nums):
                return 0
            
            if idx in count:
                return count[idx]
            else:
                count[idx] = max(nums[idx] + dfs(idx + 2), dfs(idx + 1))
                return count[idx]

        return dfs(0)