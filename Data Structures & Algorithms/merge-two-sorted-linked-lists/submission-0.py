# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current1 = list1
        current2 = list2

        if current1 == None:
            return list2
        
        if current2 == None:
            return list1


        if current1.val <= current2.val:
            output = current1
            current1 = current1.next
        else:
            output = current2
            current2 = current2.next

        out_current = output
        while current1 != None and current2 != None:
            if current1.val <= current2.val:
                out_current.next = current1
                out_current = current1
                current1 = current1.next
            else:
                out_current.next = current2
                out_current = current2
                current2 = current2.next
        
        if current1 != None:
            out_current.next = current1
        else:
            out_current.next = current2

        return output
                


