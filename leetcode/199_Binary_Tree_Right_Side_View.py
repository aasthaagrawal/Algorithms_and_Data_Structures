#https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        levq=[root]
        nextlevq=[]
        rsView=[]
        while len(levq):
            while len(levq):
                ele=levq.pop(0)
                if len(levq)==0:
                    rsView.append(ele.val)
                if ele.left:
                    nextlevq.append(ele.left)
                if ele.right:
                    nextlevq.append(ele.right)
            levq=nextlevq
            nextlevq=[]
        return rsView
