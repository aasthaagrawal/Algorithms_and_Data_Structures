#https://leetcode.com/problems/valid-palindrome/submissions/
#Complexity: O(n)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.translate(s.maketrans('','',string.punctuation))
        s=s.lower().replace(' ','')
        return (s==s[::-1])
