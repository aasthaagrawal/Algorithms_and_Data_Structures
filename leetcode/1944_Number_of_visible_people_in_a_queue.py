#https://leetcode.com/problems/number-of-visible-people-in-a-queue/
#Time complexity: O(N)
#Space complexity: O(N)

class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        st = [heights[-1]]
        solution = [0]*n
        for i in range(n-2,-1,-1):
            count = 0
            while st and st[-1]<heights[i]:
                st.pop()
                count += 1
            if len(st)>0:
                count += 1
            solution[i] = count
            st.append(heights[i])
        return solution
