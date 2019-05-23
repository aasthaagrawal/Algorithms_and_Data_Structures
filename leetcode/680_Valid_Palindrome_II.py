#https://leetcode.com/problems/valid-palindrome-ii/
#Complexity: O(n)

class Solution:
    def checkPalindrome(self, s:str) -> bool:
        return (s==s[::-1])
    def validPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1
        while(i<j):
            if s[i]!=s[j]:
                break
            i+=1
            j-=1
        if i>=j:
            return True
        else:
            return (self.checkPalindrome(s[i+1:j+1]) or self.checkPalindrome(s[i:j]))
