class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                curr = stack.pop()
                if stack:
                    area = (i - stack[-1] - 1) * heights[curr]
                else:
                    area = (i) * heights[curr]
                maxArea = max(area, maxArea)

            stack.append(i)
        
        while stack:
            curr = stack.pop()
            if stack:
                area = heights[curr] * (len(heights) - stack[-1] - 1)
            else:
                area = heights[curr] * (len(heights))
            maxArea = max(area, maxArea)
        
        return maxArea