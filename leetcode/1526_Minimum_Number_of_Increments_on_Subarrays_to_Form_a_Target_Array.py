#https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/
#Time Complexity: O(n)

class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        total_op = 0
        latest_op = 0
        for num in target:
            if num>latest_op:
                total_op += (num-latest_op)
            latest_op = num
        return total_op
