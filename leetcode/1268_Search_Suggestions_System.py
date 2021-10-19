#https://leetcode.com/problems/search-suggestions-system/
#Space Complexity: Space required for trie O(26x) where x is the number of nodes in trie [O(nm) where n = num of products and m = max product name length] and space required for the output = O(s) where s is the length of search word
#Time Complexity: Insert of all products takes O(nm); If s=len(prefix), we run O(s) times findSuggestions. Each FindSuggestion takes O(s + 26m) [It wouldn't exactly be m but number of successors of node where prefix is found)]
#https://stackoverflow.com/questions/64574941/what-is-the-time-complexity-of-arrays-sortstring/64575094#64575094
#https://leetcode.com/problems/search-suggestions-system/discuss/1024115/Lessons-learned

class TrieNode:
    def __init__(self):
        self.isLeafNode = False
        self.chars = [None]*26

class Trie:
    def __init__(self):
        self.root = self.getTrieNode()

    def getTrieNode(self):
        return TrieNode()

    def charToIndex(self,ch):
        return ord(ch)-97

    def insert(self, word):
        node =self.root
        for i in range(len(word)):
            ch_i = self.charToIndex(word[i])
            if node.chars[ch_i] == None:
                node.chars[ch_i] = self.getTrieNode()
            node = node.chars[ch_i]
        node.isLeafNode = True

    def findFirstN(self, node, st, result, N=3):
        if len(result) == N:
            return result

        if node.isLeafNode:
            result.append(st)

        for ch_i in range(26):
            if node.chars[ch_i] is not None:
                result = self.findFirstN(node.chars[ch_i],st+chr(97+ch_i),result,N)
                if len(result)==N:
                    return result
        return result

    def findSuggestions(self, prefix):
        node = self.root
        for i in range(len(prefix)):
            ch_i = self.charToIndex(prefix[i])
            if not node.chars[ch_i]:
                return []
            node = node.chars[ch_i]

        return self.findFirstN(node,prefix,[],3)


class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = Trie()
        for product in products:
            trie.insert(product)

        result = []
        for i in range(1,len(searchWord)+1):
            result.append(trie.findSuggestions(searchWord[:i]))
        return result
