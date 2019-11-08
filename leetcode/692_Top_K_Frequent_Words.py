#https://leetcode.com/problems/top-k-frequent-words/

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d={}
        for word in words:
            if word in d:
                d[word]+=1
            else:
                d[word]=1
        ls=sorted(d.items(),key=lambda x:(-x[1],x[0]))[:k]
        result=[]
        for i in ls:
            result.append(i[0])
        return result
