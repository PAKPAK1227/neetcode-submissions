# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        start, reversed_head, fast = head, head, head
        while fast.next and fast.next.next:
            start = start.next
            fast = fast.next.next
        
        reversed_head = start.next
        start.next = None




        current, prev = reversed_head, None
        while current:
            next_node = current.next
            current.next = prev
            prev = current 
            current = next_node
        reversed_head = prev

        left = head
        while left and reversed_head:
            left_next_node = left.next
            reversed_next_node = reversed_head.next
            left.next = reversed_head
            reversed_head.next = left_next_node
            reversed_head = reversed_next_node
            left = left_next_node

        
     
            

        

        
        