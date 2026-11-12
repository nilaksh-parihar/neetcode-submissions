# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        if not list1:
            return list2
        if not list2:
            return list1
        
        if list1.val <= list2.val:
            dummy = list1
            curr = dummy
            nxt = list2
        else:
            dummy = list2
            curr = dummy
            nxt = list1

        while curr.next and nxt:
            if curr.next.val >= nxt.val:
                temp = curr.next
                curr.next = nxt
                curr = nxt
                nxt = temp
            else :
                curr = curr.next

        if not curr.next:
            curr.next = nxt

        return dummy
