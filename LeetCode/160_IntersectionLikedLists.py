# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        la = 0
        lb = 0
        na = headA
        nb = headB
        while na:
            na=na.next
            la+=1
        while nb:
            nb=nb.next
            lb+=1
        nb = headB
        na = headA
        if la>lb:
            for _ in range(la-lb):
                na=na.next
        elif lb>la:
            for _ in range(lb-la):
                nb=nb.next
        while na:
            if na == nb:
                return na
            na = na.next
            nb = nb.next
        return None
        
# https://leetcode.com/problems/intersection-of-two-linked-lists/