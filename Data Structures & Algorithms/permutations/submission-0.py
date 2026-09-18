class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums[:]]  # base case: one element = one permutation

        res = []
        for i in range(len(nums)):
            rest = nums[:i] + nums[i+1:]
            for perm in self.permute(rest):
                res.append(perm + [nums[i]])
        return res