# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        nodes =[]
        for node in lists:
            head = node
            while head:
                nodes.append(head.val)
                head=head.next
        
        nodes.sort()
        res = ListNode(0)
        r1= res
        for n in nodes:
            r1.next = ListNode(n)
            r1=r1.next

        return res.next
