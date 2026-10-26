# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        hasht = set()

        while head and head not in hasht:

            hasht.add(head)
            head = head.next
        if not head:
            return False
        else:
            return True

        