class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[0] <= target <= row[-1]:
                left = 0
                right = len(row)

                if left < right:
                    while left < right:
                        mid = (left + right) // 2
                        if row[mid] == target:
                            return True
                        elif row[mid] > target:
                            right = mid
                        else:
                            left = mid + 1
        return False
