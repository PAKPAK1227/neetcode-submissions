# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current, prev = head, None
        # None is falsy so you can just do while current
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next    
        return prev
            
        