#https://leetcode.com/problems/palindrome-number/
#Complexity: O(n) where n is the number of digits in the integer

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        old_x = x
        new_x = 0
        while x:
            remainder = x%10
            x //= 10
            new_x = new_x*10 + remainder
        return old_x == new_x
