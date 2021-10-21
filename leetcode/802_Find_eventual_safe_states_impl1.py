#https://leetcode.com/problems/find-eventual-safe-states/
#Space Complexity: O(V+E)
#Time Complexity: O(V+E)

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe = []
        numNodes = len(graph)
        rgraph = [[] for i in range(numNodes)]
        for i in range(numNodes):
            if not graph[i]:
                safe.append(i)
            for ele in graph[i]:
                rgraph[ele].append(i)

        i = 0
        while i<len(safe):
            node = safe[i]
            for reverseEdge in rgraph[node]:
                graph[reverseEdge].remove(node)
                if len(graph[reverseEdge])==0:
                    safe.append(reverseEdge)
            i += 1
        safe = sorted(safe)
        return safe
