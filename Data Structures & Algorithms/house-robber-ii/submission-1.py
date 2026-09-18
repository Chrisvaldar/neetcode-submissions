class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        rob1 = nums[:len(nums)-1]
        rob2 = nums[1:]

        def dfs(i, arr, cache):
            if i >= len(arr):
                return 0
            if i in cache:
                return cache[i]
            cache[i] = max(arr[i] + dfs(i+2, arr, cache), dfs(i+1, arr, cache))
            return cache[i]
        
        return max(dfs(0, rob1, {}), dfs(0, rob2, {}))