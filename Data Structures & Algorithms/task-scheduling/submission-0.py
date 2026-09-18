from collections import defaultdict
import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = defaultdict(int)
        for task in tasks:
            count[task] += 1
        count = [(v, k) for k, v in count.items()]

        heapq.heapify_max(count)

        time = 0
        queue = deque()
        
        #(task, count, time)
        while count or queue:
            
            if queue and queue[0][2] == time:
                c, t, ti = queue.popleft()
                heapq.heappush_max(count, (c,t))
            
            if not count:
                time += 1
                continue

            currCount, currTask = heapq.heappop_max(count)
            
            if int(currCount) - 1 > 0:
                queue.append((currCount - 1, currTask, time + n + 1))
            time += 1
        
        return time


        

