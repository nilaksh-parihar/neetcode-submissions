# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummy = ListNode(0)
        current = dummy
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            num = v1 + v2 + carry
            carry = num // 10
            digit = num % 10

            newNode = ListNode(digit)
            current.next = newNode
            current = current.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next