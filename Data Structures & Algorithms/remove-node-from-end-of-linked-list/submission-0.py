# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        temp = head
        length = 0
        while temp:
            temp = temp.next
            length += 1

        if length - n == 0:
            temp = head.next 
            head.next = None
            return temp

        pos = 1
        temp = head
        while pos <= length - n:
            if pos == length - n:
                temp.next = temp.next.next
                return head
            temp = temp.next
            pos += 1
        return None