#https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        reverse=False
        level=[root]
        result=[]
        toggle=False
        while len(level):
            auxresult=[]
            nextLevel=[]
            while len(level):
                ele=level.pop(0)
                auxresult.append(ele.val)
                if ele.left:
                    nextLevel.append(ele.left)
                if ele.right:
                    nextLevel.append(ele.right)
            level=nextLevel
            nextLevel=[]
            if toggle:
                result.append(reversed(auxresult))
            else:
                result.append(auxresult)
            toggle=not toggle
        return result
