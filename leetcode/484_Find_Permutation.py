#https://leetcode.com/problems/find-permutation/
#Time Complexity: O(n)
#Space Complexity: O(n)

class Solution:
    def findPermutation(self, s: str) -> List[int]:
        base_val = 2
        st = [1]
        result = []

        for ele in s:
            if ele == "I":
                while st:
                    result.append(st.pop())
                st.append(base_val)
                base_val += 1
            else:
                st.append(base_val)
                base_val += 1
        while st:
            result.append(st.pop())
        return result
