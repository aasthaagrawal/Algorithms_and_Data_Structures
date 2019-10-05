#https://leetcode.com/problems/find-largest-value-in-each-tree-row/
#Complexity: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if root==None:
            return []
        q=[]
        q.append(root)
        q.append("Null")
        result=[]
        maxTillNow=float("-inf")
        while len(q):
            ele=q.pop(0)
            if ele=="Null":
                if len(q):
                    q.append("Null")
                result.append(maxTillNow)
                maxTillNow=float("-inf")
            else:
                maxTillNow=max(maxTillNow,ele.val)
                if ele.left:
                    q.append(ele.left)
                if ele.right:
                    q.append(ele.right)
        return result
