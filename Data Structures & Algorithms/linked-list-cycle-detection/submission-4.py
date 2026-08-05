# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        mylist = set()

        current = head

        while current != None:
            if current in mylist:
                return True
            
            mylist.add(current)
            current = current.next

        return False