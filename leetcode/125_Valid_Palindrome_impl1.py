#https://leetcode.com/problems/valid-palindrome/
#Complexity: O(n)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        lenS=len(s)
        if lenS==1 or lenS==0:
            return True
        i=0
        j=lenS-1
        while(i<j):
            if not s[i].isalnum():
                i+=1
            elif not s[j].isalnum():
                j-=1
            else:
                if s[i]==s[j]:
                    i+=1
                    j-=1
                else:
                    return False
        return True
