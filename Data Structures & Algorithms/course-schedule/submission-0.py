from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        q = deque()
        indegrees = defaultdict(int)
        prereqs = defaultdict(list)
        for i in range(len(prerequisites)):
            indegrees[prerequisites[i][0]] += 1
            prereqs[prerequisites[i][1]].append(prerequisites[i][0])
        
        for v in range(numCourses):
            if indegrees[v] == 0:
                q.append(v)

        courseCount = len(q)
        while q:
            curr = q.popleft()
            for unlocked in prereqs[curr]:
                indegrees[unlocked] -= 1
                if indegrees[unlocked] == 0:
                    q.append(unlocked)
                    courseCount += 1
        return courseCount == numCourses