#https://leetcode.com/problems/find-the-town-judge/
#Time complexity: O(T+N) where T is the length of trust array
#Space complexity: O(2N) or O(N)

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        isTrustedBy = {i: [] for i in range(1,N+1)}
        trustsSomeone = set([i for i in range(1,N+1)])
        for t in trust:
            trustsSomeone.discard(t[0])
            isTrustedBy[t[1]].append(t[0])
        for ele in trustsSomeone:
            if len(isTrustedBy[ele]) == N-1:
                return ele
        return -1
