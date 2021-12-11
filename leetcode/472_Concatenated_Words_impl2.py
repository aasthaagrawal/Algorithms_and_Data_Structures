#https://leetcode.com/problems/concatenated-words/
#Time complexity: O(mn)

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        if "" in words:
            words.remove("")
        self.wordSet = set(words)
        result = []
        self.d = {}
        for word in words:
            if self.dfs(word):
                result.append(word)
        return result

    def dfs(self, word):
        if word in self.d:
            return self.d[word]
        for i in range(len(word)):
            prefix, suffix = word[:i], word[i:]
            if prefix in self.wordSet and suffix in self.wordSet:
                self.d[word] = True
                return True
            elif prefix in self.wordSet and self.dfs(suffix):
                self.d[word] = True
                return True
        self.d[word] = False
        return False
