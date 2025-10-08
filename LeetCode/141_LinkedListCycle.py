# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Hare and turtoise algorithm
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hare = head
        turtle = head

        while hare and hare.next:
            turtle = turtle.next
            hare = hare.next.next
            if turtle == hare:
                return True
        return False
# https://leetcode.com/problems/linked-list-cycle/description/
