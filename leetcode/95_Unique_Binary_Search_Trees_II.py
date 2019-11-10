#https://leetcode.com/problems/unique-binary-search-trees-ii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n==0:
            return []
        return self.util(1,n)
        
    def util(self,l,r):
        result=[]
        if r<l:
            return None
        if r==l:
            result.append(TreeNode(l))
            return result
        for i in range(l,r+1):
            left=self.util(l,i-1)
            right=self.util(i+1,r)
            if left is not None and right is not None:
                for le in left:
                    for ri in right:
                        fHead=TreeNode(i)
                        fHead.left=le
                        fHead.right=ri
                        result.append(fHead)
            elif left is not None:
                for le in left:
                    fHead=TreeNode(i)
                    fHead.left=le
                    result.append(fHead)
            elif right is not None:
                for ri in right:
                    fHead=TreeNode(i)
                    fHead.right=ri
                    result.append(fHead)
        return result
