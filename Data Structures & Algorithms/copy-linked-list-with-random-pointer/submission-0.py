"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        check = {None: None}
        curr = head

        while curr:
            check[curr] = Node(curr.val, curr.next, curr.random)
            curr = curr.next
        
        curr = head
        while curr:
            check[curr].random = check[curr.random]
            check[curr].next = check[curr.next]
            curr = curr.next
        
        return check[head]