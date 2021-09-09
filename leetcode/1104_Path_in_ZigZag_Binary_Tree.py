#https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/
#Complexity: O(log n)

class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        res = []
        cur_node_level = 1
        while (2**cur_node_level -1)< label:
            cur_node_level += 1
        while cur_node_level>= 1:
            res.append(label)
            label = (2**cur_node_level - 1) + (2**(cur_node_level - 1)) - label
            label //= 2
            cur_node_level -= 1
        return reversed(res)
