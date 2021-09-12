#https://leetcode.com/problems/di-string-match/
#Time Complexity: O(n) where n=length of s
#Space Complexity: O(n) where n=length of s

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        high_pointer = len(s)
        result = []
        low_pointer = 0
        for char in s:
            if char == "I":
                result.append(low_pointer)
                low_pointer += 1
            else:
                result.append(high_pointer)
                high_pointer -= 1
        result.append(low_pointer)
        return result
