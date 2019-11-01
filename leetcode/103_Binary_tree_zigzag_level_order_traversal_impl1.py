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
        s1=[]
        s2=[]
        result=[]
        s1.append(root)
        while len(s1) or len(s2):
            auxresult=[]
            if len(s1):
                while len(s1):
                    ele=s1.pop(-1)
                    auxresult.append(ele.val)
                    if ele.left:
                        s2.append(ele.left)
                    if ele.right:
                        s2.append(ele.right)
            elif len(s2):
                while len(s2):
                    ele=s2.pop(-1)
                    auxresult.append(ele.val)
                    if ele.right:
                        s1.append(ele.right)
                    if ele.left:
                        s1.append(ele.left)
            result.append(auxresult)
        return result
