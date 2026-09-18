class Solution:
    def rob(self, nums: List[int]) -> int:
        maxMoney = 0
        count = dict()
        def dfs(idx):
            if idx >= len(nums):
                return 0
            
            if idx in count:
                return count[idx]
            else:
                count[idx] = max(nums[idx] + dfs(idx + 2), dfs(idx + 1))
                return count[idx]

        for i in range(len(nums)):
            maxMoney = max(maxMoney, dfs(i))
        return maxMoney