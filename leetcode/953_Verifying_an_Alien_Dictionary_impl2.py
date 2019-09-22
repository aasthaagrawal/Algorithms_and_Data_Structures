#https://leetcode.com/problems/verifying-an-alien-dictionary/
#Complexity:

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d={order[i]:i for i in range(len(order))}
        wNums=[[d[c] for c in word] for word in words]
        return all(w1<w2 for w1,w2 in zip(wNums,wNums[1:]))
