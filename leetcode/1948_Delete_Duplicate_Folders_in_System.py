#https://leetcode.com/problems/delete-duplicate-folders-in-system/
#Time complexity: O(nm) where n is the number of paths, m is the length of longest path

from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.child = defaultdict(TrieNode)
        self.markForDelete = False

    def insertPath(self, path):
        cur = self
        for ch in path:
            cur = cur.child[ch]

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        self.trieRoot, self.seenDict, self.out = TrieNode(), defaultdict(list), []
        for path in sorted(paths):
            self.trieRoot.insertPath(path)
        self.serialize(self.trieRoot)

        for key,val in self.seenDict.items():
            if len(val) > 1:
                for node in val:
                    node.markForDelete = True

        self.printTrie(self.trieRoot, [])
        self.out.remove([])
        return self.out

    def serialize(self, node):
        if not node.child:
            return ""
        ss = []
        for key,child in node.child.items():
            ss.append(key + ":" + self.serialize(child))
        ss_combined = "(" + "".join(ss) + ")"
        self.seenDict[ss_combined].append(node)
        return ss_combined

    def printTrie(self, node, path):
        if not node or node.markForDelete:
            return
        self.out.append(path[:])
        for ch, val in node.child.items():
            path.append(ch)
            self.printTrie(val, path)
            path.pop()
