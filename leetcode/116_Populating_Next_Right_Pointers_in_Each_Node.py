#https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return
        curQ = [root]
        nextQ = []
        while curQ:
            while curQ:
                node = curQ.pop(0)
                if curQ:
                    node.next = curQ[0]
                if node.left:
                    nextQ.append(node.left)
                if node.right:
                    nextQ.append(node.right)
            curQ = nextQ
            nextQ = []
        return root
