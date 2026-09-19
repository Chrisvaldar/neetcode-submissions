class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right  = 0, len(nums) - 1
        minVal = nums[left]

        while left < right:
            if nums[left] < nums[right]:
                return nums[left]

            mid = (left + right) // 2
            minVal = min(nums[mid], minVal)
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid
        return min(minVal, nums[left])
            
