#https://leetcode.com/problems/find-the-town-judge/
#Time Complexity: O(T+N) where T is the lenght of trust and N is the number of elements/people
#Space Complexity: O(N) {since O(2N)}

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        indegree = {i: 0 for i in range(1,N+1)}
        outdegree = {i: 0 for i in range(1,N+1)}
        for t in trust:
            outdegree[t[0]] += 1
            indegree[t[1]] += 1
        for i in range(1,N+1):
            if outdegree[i]==0 and indegree[i]==N-1:
                return i
        return -1 
