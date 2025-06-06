# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        l = head
        n = 0
        while l.next:
            n += 1
            l = l.next
        n += 1

        l.next = head
        k = k%n
        while n>k:
            n-=1
            l = l.next

        head = l.next
        l.next = None
        
        return head
        
# https://leetcode.com/problems/rotate-list