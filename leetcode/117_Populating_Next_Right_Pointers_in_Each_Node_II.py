#https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        level=[]
        nextL=[]
        level.append(root)
        while len(level)>0:
            while len(level):
                ele=level.pop(0)
                npointer=None
                if len(level):
                    npointer=level[0]
                ele.next=npointer
                if ele.left:
                    nextL.append(ele.left)
                if ele.right:
                    nextL.append(ele.right)
            level=nextL
            nextL=[]
        #return root
