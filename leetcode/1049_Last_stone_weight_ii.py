#https://leetcode.com/problems/last-stone-weight-ii/
#GeeksForGeeks solution: https://www.geeksforgeeks.org/partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum/
#Time Complexity: O(n*sum_of_stone_weight)
#Space Complexity: O(n*sum_of_stone_weight)


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        half_total = total//2
        n = len(stones)
        dp = [[False for j in range(half_total+1)] for i in range(n+1)]
        
        for i in range(n+1):
            dp[i][0] = True

        for i in range(1,n+1):
            for j in range(1,half_total+1):
                dp[i][j] = dp[i-1][j]
                if j>=stones[i-1] and dp[i-1][j-stones[i-1]]:
                    dp[i][j] = True   
                    
        result = total 
        for j in range(half_total,-1,-1):
            if dp[n][j]:
                result = total-j*2
                break
        return result
