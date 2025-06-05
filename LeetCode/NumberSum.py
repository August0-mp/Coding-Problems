# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        l = ListNode()
        ll = l
        while l1 or l2 or carry:
            t = carry
            if l1:
                t+=l1.val
                l1=l1.next
            if l2:
                t+=l2.val
                l2=l2.next
            n = t%10
            carry = t//10
            ll.next = ListNode(n)
            ll = ll.next
        return l.next

    # https://leetcode.com/problems/add-two-numbers/