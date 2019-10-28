#https://leetcode.com/problems/reverse-string-ii/
#Complexity: O(n)

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n=len(s)
        l=list(s)
        i=0
        while i<n:
            j=i+k-1
            if j<n:
                newI=j+1
            else:
                j=n-1
                newI=n
            while i<j:
                l[i],l[j]=l[j],l[i]
                i+=1
                j-=1
            i=newI+k
        return ''.join(l)
