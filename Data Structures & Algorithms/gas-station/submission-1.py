class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        i = 0
        runningDiff = 0
        start = 0
        while i < len(gas):
            diff = gas[i] - cost[i]
            runningDiff += diff

            if runningDiff < 0:
                runningDiff = 0
                start = i + 1
            i += 1
        return start
        
        