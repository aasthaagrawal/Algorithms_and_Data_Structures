#https://leetcode.com/problems/combinations/
#Time Complexity: O(2^n)

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.k = k
        self.n = n
        self.result = []
        self.getCombinations(1, [])
        return self.result
    
    def getCombinations(self, i, st):
        if i>self.n:
            if len(st)==self.k:
                self.result.append(st[:])
            return
        st.append(i)
        self.getCombinations(i+1, st)
        st.pop()
        self.getCombinations(i+1, st)
