#https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        d={}
        level=[(root,0)]
        while len(level):
            nextLevel=[]
            while len(level):
                tup=level.pop(0)
                try:
                    d[tup[1]].append(tup[0].val)
                except:
                    d[tup[1]]=[tup[0].val]
                if tup[0].left:
                    nextLevel.append((tup[0].left,tup[1]-1))
                if tup[0].right:
                    nextLevel.append((tup[0].right,tup[1]+1))
            level=sorted(nextLevel,key=lambda x:(x[1],x[0].val))
            nextLevel=[]
        result=[]
        for key in sorted(d.keys()):
            result.append(d[key])
        return result
