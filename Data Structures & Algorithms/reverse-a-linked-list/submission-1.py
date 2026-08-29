# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        
        res1 = None
        res2 = head
        while res2:
            a=res2.next
            res2.next = res1
            res1 = res2
            res2 = a
        return res1


            



        