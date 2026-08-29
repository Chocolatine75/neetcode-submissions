# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 == None and list2 ==None:
            return None
        head = ListNode()
        res =head
        while list1 != None or list2 != None:
            if list2 == None:
                res.next = list1
                list1 = list1.next
            elif list1 == None:
                res.next = list2
                list2 = list2.next
            elif list1.val <= list2.val:
                res.next = list1
                list1 = list1.next
            else:
                res.next = list2
                list2 = list2.next
            
            res = res.next
        return head.next
            


        