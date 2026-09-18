class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def subset(nums):
            if not len(nums):
                return [[]]
            
            without_last = subset(nums[:-1])
            res = []
            for thing in without_last:
                res.append(thing + [nums[-1]])
            return res + without_last

        return subset(nums)
            

                