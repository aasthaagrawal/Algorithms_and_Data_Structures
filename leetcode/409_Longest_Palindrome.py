#https://leetcode.com/problems/longest-palindrome/

class Solution:
    def longestPalindrome(self, s: str) -> int:
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        count=0
        cOdd=0
        biggestOdd=0
        for key,val in d.items():
            if val%2==0:
                count+=val
            else:
                cOdd+=1
                count+=(val-1)
        if cOdd>0:
            count+=1
        return count
