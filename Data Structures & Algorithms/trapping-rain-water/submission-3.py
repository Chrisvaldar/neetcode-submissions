class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        totalWater = 0
        leftMax = height[left]
        rightMax = height[right]

        while left < right:
            if height[left] < height[right]:
                leftMax = max(height[left], leftMax)
                totalWater += (leftMax - height[left])
                left += 1
            else:
                rightMax = max(height[right], rightMax)
                totalWater += (rightMax - height[right])
                right -= 1
        return totalWater



