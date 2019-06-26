#https://leetcode.com/problems/third-maximum-number/

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        sN=set(nums)
        lN=len(sN)
        if lN<3:
            return max(sN)
        sN.remove(max(sN))
        sN.remove(max(sN))
        return max(sN)
