import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pointTuples = []
        for point in points:
            pointTuples.append((((point[0])**2+ (point[1]**2))**0.5, point))
        heapq.heapify(pointTuples)

        res = []
        for _ in range(k):
            res.append(heapq.heappop(pointTuples)[1])

        return res