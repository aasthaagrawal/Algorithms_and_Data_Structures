#https://leetcode.com/problems/serialize-and-deserialize-bst/
#Time Complexity: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return ""
        res = str(root.val)
        if root.left:
            res = res + "," + self.serialize(root.left)
        if root.right:
            res = res + "," + self.serialize(root.right)
        return res


    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if len(data) == 0:
            return None
        data = data.split(",")
        data = [int(c) for c in data]
        i, root = self.util(data, 0, -float("inf"), float("inf"), len(data))
        return root

    def util(self, data, i, low, high, n):
        if i==n:
            return i, None
        root = None
        if low<data[i]<high:
            root = TreeNode(data[i])
            i += 1
            i, root.left = self.util(data, i, low, root.val, n)
            i, root.right = self.util(data, i, root.val, high, n)
        return i, root



# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
