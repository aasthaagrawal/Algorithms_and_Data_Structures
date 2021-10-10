#https://leetcode.com/problems/reverse-prefix-of-word/
#Complexity: O(n)

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        n = len(word)
        index = 0
        while index<n:
            if word[index]==ch:
                break
            index += 1
        if index==n:
            return word
        index += 1
        return ''.join(reversed(word[:index])) + word[index:]
