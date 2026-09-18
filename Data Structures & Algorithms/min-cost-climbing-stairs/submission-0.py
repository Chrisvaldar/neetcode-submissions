class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a, b = 0, 0  # a = dp[i-2], b = dp[i-1]
        for i in range(2, len(cost) + 1):
            a, b = b, min(b + cost[i-1], a + cost[i-2])
        return b
