class MyLinkedList:

    class Node:
        def __init__(self, val=0, nxt=None):
            self.val = val
            self.next = nxt

    def __init__(self):
        self.head = MyLinkedList.Node() 
        self.size = 0

    def _prev(self, index):
        node = self.head
        for _ in range(index):
            node = node.next
        return node

    def get(self, index: int) -> int:
        if not 0 <= index < self.size:
            return -1
        return self._prev(index).next.val

    def addAtHead(self, val: int) -> None:
        self.head.next = MyLinkedList.Node(val, self.head.next)
        self.size += 1

    def addAtTail(self, val: int) -> None:
        node = self.head
        while node.next:
            node = node.next
        node.next = MyLinkedList.Node(val)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if not 0 <= index <= self.size:
            return
        prev = self._prev(index)
        prev.next = MyLinkedList.Node(val, prev.next)
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if not 0 <= index < self.size:
            return
        prev = self._prev(index)
        prev.next = prev.next.next
        self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)