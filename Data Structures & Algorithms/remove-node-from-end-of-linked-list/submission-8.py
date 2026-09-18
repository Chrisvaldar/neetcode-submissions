# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        final = head
        start = head
        counter = 0
        while head:
            head = head.next
            counter += 1

        if n == counter:
            return start.next
        for _ in range(counter - n - 1):
            start = start.next
            
        start.next = start.next.next
        return final

