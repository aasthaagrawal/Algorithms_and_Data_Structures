#https://leetcode.com/problems/daily-temperatures/
#Time Complexity: O(N)
#Space Complexity: O(N)

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        result = [0]*len(temperatures)
        for ind,temp in enumerate(temperatures):
            while st and temperatures[st[-1]]<temp:
                poped_i = st.pop()
                result[poped_i] = ind - poped_i
            st.append(ind)
        return result
