#https://leetcode.com/problems/find-and-replace-pattern/

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        l=len(pattern)
        result=[]
        for word in words:
            flag=True
            d_pat={}
            d_word={}
            for i in range(l):
                if pattern[i] in d_pat:
                    if d_pat[pattern[i]]!=word[i]:
                        flag=False
                        break
                else:
                    d_pat[pattern[i]]=word[i]
                if word[i] in d_word:
                    if d_word[word[i]]!=pattern[i]:
                        flag=False
                        break
                else:
                    d_word[word[i]]=pattern[i]
            if flag:
                result.append(word)
        return result
