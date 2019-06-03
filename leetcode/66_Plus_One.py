#https://leetcode.com/problems/plus-one/
#Complexity=O(len(digits))

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length=len(digits)-1
        carry=1
        while length>=0:
            sumNum=digits[length]+carry
            digits[length]=sumNum%10
            carry=sumNum//10
            length-=1
            if carry==0:
                break
        if carry>0:
            return [carry]+digits
        return digits
