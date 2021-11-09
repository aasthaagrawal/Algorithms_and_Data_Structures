#https://leetcode.com/problems/check-if-two-expression-trees-are-equivalent/
#Time complexity: O(n)
#Space Complexity: O(n)

# Definition for a binary tree node.
# class Node(object):
#     def __init__(self, val=" ", left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEquivalence(self, root1: 'Node', root2: 'Node') -> bool:
        operands = defaultdict(int)
        q = [root1]
        while q:
            ele = q.pop(0)
            if not ele.left and not ele.right:
                operands[ele.val] += 1
            else:
                if ele.left:
                    q.append(ele.left)
                if ele.right:
                    q.append(ele.right)
        q = [root2]
        while q:
            ele = q.pop(0)
            if not ele.left and not ele.right:
                if operands[ele.val] <= 0:
                    return False
                operands[ele.val] -= 1
            else:
                if ele.left:
                    q.append(ele.left)
                if ele.right:
                    q.append(ele.right)
        return True
