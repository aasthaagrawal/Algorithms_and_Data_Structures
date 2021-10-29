#https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/
#Time Complexity: O(N)

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return root
        self.head = None
        self.last_node_processed = None
        self.util(root)
        if self.last_node_processed.right != self.head:
            self.last_node_processed.right = self.head
            self.head.left = self.last_node_processed
        return self.head

    def util(self, node):
        if not node:
            return
        self.util(node.left)

        if self.last_node_processed:
            node.left = self.last_node_processed
            self.last_node_processed.right = node
        else:
            self.head = node
        self.last_node_processed = node

        self.util(node.right)
