#https://leetcode.com/problems/shortest-word-distance-iii/
#Time complexity: O(n)

class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        last_1,last_2 = None, None
        output = float("inf")
        same = word1 == word2
        for i,word in enumerate(wordsDict):
            if word == word1:
                if same:
                    last_2 = last_1
                last_1 = i
                if last_2 != None:
                    output = min(output,abs(last_1-last_2))
            elif word == word2:
                last_2 = i
                if last_1 != None:
                    output = min(output,abs(last_1-last_2))
        return output
