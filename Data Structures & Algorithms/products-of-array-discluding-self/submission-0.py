class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        for i in range(len(nums)):
            total = None
            for j in range(len(nums)):
                if j == i:
                    continue
                if total is None:
                    total = nums[j]
                else:
                    total *= nums[j]
            output.append(total)
            
        return output