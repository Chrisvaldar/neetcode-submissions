class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNums = sorted(nums)
        res = []

        for i in range(len(sortedNums)):
            left = i + 1
            right = len(sortedNums) - 1
            triple = None

            while left < right:
                total = sortedNums[i] + sortedNums[left] + sortedNums[right]
                if total == 0:
                    triple = [sortedNums[i], sortedNums[left], sortedNums[right]]
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
                
                if triple and triple not in res:
                    res.append(triple)
                    triple = None
        return res
