class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low = 0
        high = len(numbers) - 1

        while low < high:
            total = numbers[high] + numbers[low]

            if total < target:
                low += 1
            elif total > target:
                high -= 1
            else:
                return [low+1,high+1]
        return [low, high]