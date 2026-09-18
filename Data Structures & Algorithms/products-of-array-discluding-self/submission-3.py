class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        for k in range(1, len(nums)):
            prefix.append(nums[k-1] * prefix[-1])
        print(prefix)

        sufix = [1]
        for i in range(len(nums) - 2, -1, -1):
            sufix.append(nums[i+1] * sufix[-1])
        sufix.reverse()
        print(sufix)

        res = []
        for j in range(len(nums)):
            res.append(prefix[j] * sufix[j])
        return res


