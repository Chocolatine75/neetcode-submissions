# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head == None or head.next == None:
            return None
        
        h =head
        i=0
        while h:
            i+=1
            h=h.next
        
        i = i-n
        if i ==0:
            return head.next
        r1 = head
        r2 = head
        j=0
        while j <i:
            r1 = r2
            r2 = r2.next
            j+=1
        
        r1.next = r2.next
        return head



            

        