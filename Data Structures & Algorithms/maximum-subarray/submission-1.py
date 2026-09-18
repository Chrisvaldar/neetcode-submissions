class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        maxSum = nums[0]
        currSum = nums[0]

        for i in range(1, len(nums)):
            print("maxSum: ", maxSum)
            print("currSum: ", currSum)
            best = max(currSum + nums[i], nums[i])
            currSum = best
            maxSum = max(best, maxSum)
        return maxSum
