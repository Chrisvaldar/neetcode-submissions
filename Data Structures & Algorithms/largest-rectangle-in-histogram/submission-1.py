class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        n = len(heights)

        for i in range(n):
            start = i
            while stack and heights[i] < stack[-1][0]:
                val, index = stack.pop()
                maxArea = max(maxArea, val * (i - index))
                start = index
            stack.append((heights[i], start))

        for h, j in stack:
            maxArea = max(maxArea, h * (n - j))
        
        return maxArea