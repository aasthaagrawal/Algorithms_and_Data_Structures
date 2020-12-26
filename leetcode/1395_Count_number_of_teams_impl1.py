#https://leetcode.com/problems/count-number-of-teams/
#Time complexity: O(n^2)
#Space complexity: O(1)

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        result = 0
        for i in range(len(rating)):
            ls = lb = rs = rb = 0
            for j in range(len(rating)):
                if j<i:
                    if rating[j] < rating[i]:
                        ls += 1
                    elif rating[j] > rating[i]:
                        lb += 1
                elif j>i:
                    if rating[j] < rating[i]:
                        rs += 1
                    elif rating[j] > rating[i]:
                        rb += 1
            result += (ls*rb + lb*rs)
        return result
