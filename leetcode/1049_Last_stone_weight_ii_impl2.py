#https://leetcode.com/problems/last-stone-weight-ii/
#https://www.geeksforgeeks.org/partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum/
#Time Complexity: O(n*sum_of_stones_weight)
#Space Complexity: O(sum_of_stones_weight)

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        half_total = total//2
        n = len(stones)
        dp = [False for j in range(half_total+1)]
        dp[0] = True
        
        max_sum_pos = 0
        for i in range(n):
            for j in range(half_total,0,-1):
                if j>=stones[i] and dp[j-stones[i]]:
                    dp[j]=True
                    max_sum_pos = max(max_sum_pos,j)
        
        return total-2*max_sum_pos
