#https://leetcode.com/problems/buddy-strings/
#Complexity: O(n)

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        lenA=len(A)
        if lenA!=len(B):
            return False
        i=0
        swap=2
        swapIndex=-1
        while i<lenA:
            if A[i]!=B[i]:
                if swap==2:
                    swap=1
                    swapIndex=i
                elif swap==1:
                    if A[swapIndex]==B[i] and B[swapIndex]==A[i]:
                        swap=0
                    else:
                        return False
                else:
                    return False
            i+=1
            
        if swap==0:
            return True
        else:
            h={}
            for ch in A:
                if ch in h:
                    return True
                h[ch]=0
        return False
