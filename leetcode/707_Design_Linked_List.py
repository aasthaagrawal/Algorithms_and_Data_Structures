#https://leetcode.com/problems/design-linked-list/

class SinglyLinkedListNode:
    def __init__(self, value):
        self.val = value
        self.nextNode = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """  
        i = 0
        cur = self.head
        while cur is not None:
            if i==index:
                return cur.val
            i+=1
            cur = cur.nextNode
        return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        node = SinglyLinkedListNode(val)
        if self.head is not None:
            node.nextNode = self.head
        self.head = node
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node = SinglyLinkedListNode(val)
        if self.head is None:
            self.head = node
            return
        cur = self.head
        while cur.nextNode is not None:
            cur = cur.nextNode
        cur.nextNode = node
        cur = self.head

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index == 0:
            self.addAtHead(val)
        else:
            node = SinglyLinkedListNode(val)
            i = 0
            cur = self.head
            prevNode = None
            while cur is not None:
                if i==index-1:
                    prevNode = cur
                    break
                cur = cur.nextNode
                i+=1
            if prevNode is not None:
                node.nextNode = prevNode.nextNode
                prevNode.nextNode = node

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index == 0:
            node = self.head
            self.head = node.nextNode
        else:
            cur = self.head
            i=0
            prevNode = None
            while cur is not None:
                if i==index-1:
                    prevNode = cur
                    break
                cur = cur.nextNode
                i+=1
            if prevNode is not None:
                node = prevNode.nextNode
                if node is not None:
                    prevNode.nextNode = node.nextNode
        del node
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
