#https://leetcode.com/problems/verifying-an-alien-dictionary/
#Complexity:

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d={order[i]:i for i in range(len(order))}
        for i in range(1,len(words)):
            l1=len(words[i-1])
            l2=len(words[i])
            l=min(l1,l2)
            flag=False
            for j in range(l):
                print(j)
                if words[i-1][j] is not words[i][j]:
                    flag=True
                    if d[words[i-1][j]]>d[words[i][j]]:
                        return False
                    break
            if flag==False and l1>l2:
                return False
        return True
