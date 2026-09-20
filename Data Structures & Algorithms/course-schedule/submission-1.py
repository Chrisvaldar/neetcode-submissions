from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)

        state = [0] * numCourses

        def dfs(course):
            if state[course] == 1:
                return True
            if state[course] == 2:
                return False


            state[course] = 1
            for neighbor in graph[course]:
                if dfs(neighbor):
                    return True
            state[course] = 2
            return False

        for course in range(numCourses):
            if dfs(course):
                return False
        return True
        