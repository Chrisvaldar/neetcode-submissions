class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProduct = nums[0]
        minEnd = nums[0]
        maxEnd = nums[0]

        for i in range(1,len(nums)):
            candidates = (nums[i], maxEnd * nums[i], minEnd * nums[i])
            maxEnd = max(candidates)
            minEnd = min(candidates)
            maxProduct = max(maxEnd, maxProduct)
        return maxProduct