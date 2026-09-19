class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = m * n

        while left < right:
            mid = (left + right) // 2
            midItem = matrix[mid // n][mid % n]

            if midItem == target:
                return True
            elif midItem < target:
                left = mid + 1
            else:
                right = mid
        return False