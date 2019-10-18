#https://leetcode.com/problems/remove-nth-node-from-end-of-list/
#Complexity: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        index=0
        def recUtil(node):
            if node is None:
                return 0
            index=recUtil(node.next)+1
            if index==n+1:
                node.next=(node.next).next
            return index
        index=recUtil(head)
        if index==n:
            head=head.next
        return head
