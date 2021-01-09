#https://leetcode.com/problems/count-numbers-with-unique-digits/
#Complexity: O(n)

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 10
        total = 10
        mul = 9
        index = 9
        for i in range(2,n+1):
            mul *= index
            total += mul
            index -= 1
        return total
