#https://leetcode.com/problems/word-ladder/
#Complexity:

#Timesout in leetcode submission


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        n=len(wordList)
        wLen=len(wordList[0])
        visited = [False]*n
        level=1
        q=[]
        q.append(beginWord)
        q.append("Null")
        while len(q):
            ele=q.pop(0)
            if ele is "Null":
                level+=1
                if len(q) and not all(e is"Null" for e in q):
                    q.append("Null")
            else:
                for i in range(n):
                    if visited[i]==False:
                        w=wordList[i]
                        diff=0
                        for j in range(wLen):
                            if ele[j]!=w[j]:
                                diff+=1
                                if diff>1:
                                    break
                        if diff<=1:
                            if w==endWord:
                                return level+1
                            q.append(w)
                            visited[i]=True
        return 0
