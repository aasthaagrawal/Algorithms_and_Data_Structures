#https://leetcode.com/problems/find-root-of-n-ary-tree/
#Time Complexity: O(N)
#Space Complexity: O(1)

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        total = 0
        for node in tree:
            total += node.val
            for child in node.children:
                total -= child.val
        for node in tree:
            if node.val == total:
                return node
