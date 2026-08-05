# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
            
        prev = head
        current = head.next
        nextnode =current.next
        prev.next = None

        while nextnode != None:
            current.next = prev
            prev = current
            current = nextnode
            nextnode = nextnode.next
        current.next = prev
        
        head = current
        return head