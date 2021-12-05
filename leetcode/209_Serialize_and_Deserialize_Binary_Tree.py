#https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
#Time complexity: O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        q = [root]
        res = []
        while q:
            node = q.pop(0)
            if node == None:
                res.append("None")
                continue
            res.append(str(node.val))
            q.append(node.left)
            q.append(node.right)

        while res[-1] == "None":
            res.pop()
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == "":
            return None
        new_data = []
        for i,c in enumerate(data.split(",")):
            if c == "None":
                new_data.append(None)
            else:
                new_data.append(int(c))
        data = new_data
        del new_data
        i, n = 0, len(data)
        root = TreeNode(data[i])
        i += 1
        q = [root]
        while q and i<n:
            node = q.pop(0)
            if data[i] != None:
                node.left = TreeNode(data[i])
                q.append(node.left)
            i += 1
            if i<n and data[i] != None:
                node.right = TreeNode(data[i])
                q.append(node.right)
            i += 1
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
