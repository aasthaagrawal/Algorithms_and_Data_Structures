#https://leetcode.com/problems/flower-planting-with-no-adjacent/
#Complexity:O(N)

class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        graph=[[] for i in range(N)]
        for i in paths:
            graph[i[0]-1].append(i[1]-1)
            graph[i[1]-1].append(i[0]-1)
        result=[0 for i in range(N)]
        for i in range(N):
            flowers={1,2,3,4}
            flowers-={result[j] for j in graph[i]}
            result[i]=flowers.pop()
        return result
