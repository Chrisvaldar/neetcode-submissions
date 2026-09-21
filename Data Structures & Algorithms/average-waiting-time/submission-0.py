class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        runningSum = 0
        currTime = customers[0][0]
        for customer in customers:
            if currTime >= customer[0]:
                finishTime = currTime + customer[1]
                waitTime = finishTime - customer[0]
            else:
                finishTime = customer[0] + customer[1]
                waitTime = customer[1]
            runningSum += waitTime
            currTime = finishTime
        return runningSum / len(customers)