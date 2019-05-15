#https://leetcode.com/problems/repeated-substring-pattern/
#Complexity: O(n)
#Uses KMP algo's preprocessing mechanism

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        sLen=len(s)
        
        #creating lps array
        lps = [0]*sLen
        lps[0]=0
        i=0
        j=1
        while(j<sLen):
            if s[i]==s[j]:
                i+=1
                lps[j]=i
                j+=1
            else:
                if i==0:
                    lps[j]=0
                    j+=1
                else:
                    i=lps[i-1]
        
        substringLen=sLen-lps[sLen-1]
        if lps[sLen-1]>0 and sLen%substringLen==0:
            return True
        else:
            return False
