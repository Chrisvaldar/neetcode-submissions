import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # pointTuples = []
        # for point in points:
        #     pointTuples.append((((point[0])**2+ (point[1]**2))**0.5, point))
        # heapq.heapify(pointTuples)

        # res = []
        # for _ in range(k):
        #     res.append(heapq.heappop(pointTuples)[1])

        # return res

        heap = []

        for point in points:
            dist = (-((point[0])**2+ (point[1]**2))**0.5, point)
            if len(heap) < k:
                heapq.heappush(heap, dist)
            else:
                if heap[0][0] < dist[0]:
                    heapq.heapreplace(heap, dist)
            
        return [thing[1] for thing in heap]

