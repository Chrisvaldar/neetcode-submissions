# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = None
        curr = None

        while l1 and l2:
            newNode = ListNode((l1.val + l2.val) % 10, None)
            if l1.val + l2.val > 9:
                if l1.next:
                    l1.next.val += 1
                elif l2.next:
                    l2.next.val += 1
                else: 
                    after = ListNode((l1.val + l2.val) // 10, None)
                    newNode.next = after

            if not res and not curr:
                res = newNode
                curr = newNode
            else:
                curr.next = newNode
                curr = curr.next

            l1 = l1.next
            l2 = l2.next
            
        
        while l1:
            leftover1 = ListNode(l1.val % 10, None)
            if l1.val > 9:
                if l1.next:
                    l1.next.val += 1
                else: 
                    after = ListNode(l1.val // 10, None)
                    leftover1.next = after
            curr.next  = leftover1
            curr = curr.next

            l1 = l1.next
        
        while l2:
            leftover2 = ListNode(l2.val % 10, None)
            if l2.val > 9:
                if l2.next:
                    l2.next.val += 1
                else: 
                    after = ListNode(l2.val // 10, None)
                    leftover2.next = after
            curr.next  = leftover2
            curr = curr.next

            l2 = l2.next
        
        return res
            
            

