#https://leetcode.com/problems/maximum-length-of-repeated-subarray/
#Time and space complexity: O(MN)

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        self.result = 0
        n1 = len(nums1)
        n2 = len(nums2)
        dp = [[0 for j in range(n2+1)] for i in range(n1+1)]
        for i in range(n1):
            for j in range(n2):
                if nums1[i] == nums2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                    self.result = max(self.result,dp[i+1][j+1])
        return self.result
