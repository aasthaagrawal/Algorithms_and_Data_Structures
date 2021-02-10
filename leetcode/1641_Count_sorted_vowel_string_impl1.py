#https://leetcode.com/problems/count-sorted-vowel-strings/
#Time Complexity:O(N*N!)
#Space Complexity: O(1)

class Solution:
    def countVowelStrings(self, n: int) -> int:
        self.n = n
        self.result = 0
        self.vowels = ['a', 'e', 'i', 'o', 'u']
        self.util(0,0)
        return self.result
    
    def util(self, index, substrLen):
        if substrLen == self.n:
            self.result += 1
            return
        if index == 5:
            return
        
        #include
        substrLen += 1
        self.util(index, substrLen)
        
        #dont include
        substrLen -= 1
        self.util(index+1, substrLen) 
