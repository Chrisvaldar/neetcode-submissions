import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heapq.heapify_max(nums)
        # res = 0
        # for i in range(k):
        #     res = heapq.heappop_max(nums)
        # return res

        heap = []
        for i in range(len(nums)):
            heapq.heappush(heap, nums[i])
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]