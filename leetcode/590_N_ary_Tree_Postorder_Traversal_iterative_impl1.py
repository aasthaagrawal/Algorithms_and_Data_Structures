#https://leetcode.com/problems/n-ary-tree-postorder-traversal/
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
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        stack = [root]
        res = []
        ele = None
        while stack:
            if ele and stack and ele in stack[-1].children:
                ele = stack.pop()
                res.append(ele.val)
                continue
            ele = stack[-1]
            if not ele.children:
                res.append(ele.val)
                stack.pop()
            else:
                stack.extend(reversed(ele.children))
        return res
