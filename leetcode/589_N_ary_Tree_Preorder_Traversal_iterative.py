#https://leetcode.com/problems/n-ary-tree-preorder-traversal/
#Time Complexity: O(n)
#Space Complexity: O(n)

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        #Use stack and access children right to left
        if root==None:
            return []
        stack = [root]
        res = []
        while stack:
            ele = stack.pop()
            res.append(ele.val)
            if ele.children is not None:
                stack.extend(reversed(ele.children))
        return res
