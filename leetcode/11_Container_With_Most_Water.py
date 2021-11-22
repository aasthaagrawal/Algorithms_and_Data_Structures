#https://leetcode.com/problems/container-with-most-water/
#Time Complexity: O(n)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        dist = len(height) - 1
        left, right = 0, dist
        while left < right:
            if height[left] < height[right]:
                result = max(result, dist*height[left])
                left += 1
            else:
                result = max(result, dist*height[right])
                right -= 1
            dist -= 1
        return result
