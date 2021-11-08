#https://leetcode.com/problems/find-root-of-n-ary-tree/
#Time Complexity: O(N)
#Space Complexity: O(N)

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        self.parent_dict = {}
        for node in tree:
            for child in node.children:
                self.parent_dict[child.val] = node.val
        for node in tree:
            if node.val not in self.parent_dict:
                return node
        return None
