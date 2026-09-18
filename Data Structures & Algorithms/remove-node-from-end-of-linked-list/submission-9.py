# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # final = head
        # start = head
        # counter = 0
        # while head:
        #     head = head.next
        #     counter += 1

        # if n == counter:
        #     return start.next
        # for _ in range(counter - n - 1):
        #     start = start.next
            
        # start.next = start.next.next
        # return final

        dummy =  ListNode(0, head)
        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1
        
        while right:
            right = right.next
            left = left.next
        left.next = left.next.next

        return dummy.next
