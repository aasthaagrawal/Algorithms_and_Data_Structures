#https://leetcode.com/problems/play-with-chips/
#Complexity:O(n)

class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        n=len(chips)
        num0=0
        num1=0
        for i in chips:
            if i%2==0:
                num0+=1
            else:
                num1+=1
        if n==num0 or n==num1:
            return 0
        return min(num0,num1)
