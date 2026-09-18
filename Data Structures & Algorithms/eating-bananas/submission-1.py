class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles) + 1

        while left < right:
            mid = (left + right) // 2
            total = sum([math.ceil(pile/mid) for pile in piles])

            if total <= h:
                right = mid
            else:
                left = mid + 1
        return left
