class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        totalArea = 0


        maxLeft, maxRight = 0, 0
        while left < right:
            
            maxLeft = height[left] if height[left] > maxLeft else maxLeft
            maxRight = height[right] if height[right] > maxRight else maxRight

            if height[left] < height[right]:
                totalArea += maxLeft - height[left]
                left += 1
            else:
                totalArea += maxRight - height[right]
                right -= 1

        return totalArea
        
            
            
