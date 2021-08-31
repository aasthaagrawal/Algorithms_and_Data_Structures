#https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
#Time limit exceeds
#Time complexity: O(k^n)

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        n = len(nums)
        if n<k or total%k!=0:
            return False
        total //= k
        partition = [0 for i in range(k)] 
        
        def aux(i,partition):
            if i==n:
                for j in range(k):
                    if total != partition[j]:
                        return False
                return True
            for j in range(k):
                partition[j] += nums[i]
                if aux(i+1,partition):
                    return True
                partition[j] -= nums[i]
            return False
        
        return aux(0,partition)
