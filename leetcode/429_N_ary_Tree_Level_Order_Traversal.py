#https://leetcode.com/problems/n-ary-tree-level-order-traversal/
#Complexity: O(n)


"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        nextQ = []
        curQ = [root]
        result = []
        while len(curQ)>0:
            result.append([])
            for node in curQ:
                result[-1].append(node.val)
                nextQ.extend(node.children)
            curQ = nextQ
            nextQ = []
        return result
