#https://leetcode.com/problems/binary-tree-level-order-traversal/
#Complexity: O(n+h)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result=[]
        auxResult=[]
        queue=[]
        queue.append(root)
        queue.append(None)
        
        while len(queue):
            root=queue.pop(0)
            
            if root is None:
                result.append(auxResult)
                auxResult=[]
                if len(queue):
                    queue.append(None)
            else:
                auxResult.append(root.val)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
        return result
