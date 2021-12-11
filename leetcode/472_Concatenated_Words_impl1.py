#https://leetcode.com/problems/concatenated-words/
#TIME LIMIT EXCEEDS 
#Solution uses Trie
#Time complexity: O(mn) where m is the length of words and n is length of longest word

class TrieNode:
    def __init__(self):
        self.next = [None]*26
        self.isWordEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.record = set()

    def charToIndex(self,ch):
        return ord(ch) - 97

    def insertWord(self, word):
        node = self.root
        for c in word:
            c_index = self.charToIndex(c)
            if node.next[c_index] == None:
                node.next[c_index] = TrieNode()
            node = node.next[c_index]
        node.isWordEnd = True
        self.record.add(word)

    def checkWord(self, word, num_words):
        node = self.root
        n = len(word) - 1
        for i,c in enumerate(word):
            c_index = self.charToIndex(c)
            if node.next[c_index] == None:
                return False
            node = node.next[c_index]
            if node.isWordEnd:
                num_words += 1
                #print(word, i, c, n, num_words)
                if i == n:
                    if num_words>=2:
                        return True
                    return False
                if word[i+1:] in self.record or self.checkWord(word[i+1:], num_words):
                    self.record.add(word[i+1:])
                    return True
                num_words -= 1
        return False


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        if len(words) < 3:
            return []
        result = []
        trie = Trie()
        for word in words:
            trie.insertWord(word)

        for word in words:
            if trie.checkWord(word, 0):
                result.append(word)
        return result
