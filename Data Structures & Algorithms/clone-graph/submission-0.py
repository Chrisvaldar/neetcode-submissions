"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        cloned = {}
        q = deque()

        if not node:
            return node
        initial = Node(node.val)
        q.append(node)
        cloned[node] = initial

        while q:
            curr = q.popleft()
            for n in curr.neighbors:
                if n not in cloned:
                    clone = Node(n.val)
                    cloned[n] = clone
                    q.append(n)
                cloned[curr].neighbors.append(cloned[n])
        return cloned[node]