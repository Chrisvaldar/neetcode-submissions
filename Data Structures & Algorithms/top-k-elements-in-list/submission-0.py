from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int) 
        for num in nums:
            counts[num] += 1

        tuples = [(-count, num) for num, count in counts.items()]
        heapq.heapify(tuples)
        res = []
        for i in range(k):
            res.append(heapq.heappop(tuples)[1])
        return res
        

        