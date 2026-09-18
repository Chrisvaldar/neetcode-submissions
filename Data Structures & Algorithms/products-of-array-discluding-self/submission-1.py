class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # output = []

        # for i in range(len(nums)):
        #     total = None
        #     for j in range(len(nums)):
        #         if j == i:
        #             continue
        #         if total is None:
        #             total = nums[j]
        #         else:
        #             total *= nums[j]
        #     output.append(total)
            
        # return output
        # Time complexity: O(n^2)
        # Space complexity: O(n)

        output = []

        prefix = [1]
        #prefix build
        for i in range(1, len(nums)):
            prefix.append(nums[i-1] * prefix[-1])

        suffix = [1]
        #suffix build
        for j in range(len(nums) - 2, -1, -1):
            suffix.append(suffix[-1] * nums[j + 1])
        suffix.reverse()

        for k in range(len(nums)):
            output.append(prefix[k] * suffix[k])
        return output
