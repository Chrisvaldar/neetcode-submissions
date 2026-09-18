from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = defaultdict(int)

        for i in range(len(nums)):
            if nums[i] in count:
                return [count[nums[i]], i] 
            count[target - nums[i]] = i
        
        return -1