#https://leetcode.com/problems/single-number/
#Complexity: O(n)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result=0
        for i in nums:
            result^=i
        return result
