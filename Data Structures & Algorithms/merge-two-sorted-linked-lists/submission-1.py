# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current = list1
        current2 = list2
        dummy = ListNode()
        current3 = dummy
        while current  and current2:
            if current.val < current2.val or current2 == None:
                current3.next = current
                current = current.next
            else:
                current3.next = current2
                current2 = current2.next
            
            current3 = current3.next
            
        if current:
            current3.next = current
        else:
            current3.next = current2

        return dummy.next
            
