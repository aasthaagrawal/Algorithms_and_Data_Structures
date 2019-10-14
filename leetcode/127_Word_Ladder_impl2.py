#https://leetcode.com/problems/word-ladder/
#Complexity: O(n*wLen)

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #if endword not in wordlist
        if endWord not in wordList:
            return 0
        
        #preprocessing on wordlist
        wLen=len(wordList[0])
        n=len(wordList)
        dic={}
        for word in wordList:
            for i in range(wLen):
                key=word[:i]+"*"+word[i+1:]
                if key in dic:
                    dic[key].append(word)
                else:
                    dic[key]=[word]
        
        #bfs
        level=1
        q=[]
        q.append(beginWord)
        q.append("Null")
        visited ={beginWord}
        while len(q):
            ele=q.pop(0)
            if ele is "Null":
                level+=1
                if len(q):
                    q.append("Null")
            else:
                for i in range(wLen):
                    key=ele[:i]+"*"+ele[i+1:]
                    if key in dic:
                        for w in dic[key]:
                            if w not in visited:
                                if w==endWord:
                                    return level+1
                                visited.add(w)
                                q.append(w) 
        return 0
