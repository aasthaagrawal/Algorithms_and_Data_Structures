#https://leetcode.com/problems/parallel-courses/
#Using Kahn's Algo for Topological Sort

class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph = {i:[] for i in range(n)}
        indeg = {i:0 for i in range(n)}
        for prevC, nextC in relations:
            graph[prevC-1].append(nextC-1)
            indeg[nextC-1] += 1

        nodes_with_0_indeg = set()
        for key, val in indeg.items():
            if val == 0:
                nodes_with_0_indeg.add(key)

        num_nodes_covered, minSem = 0, 0
        while nodes_with_0_indeg:
            new_num_nodes_covered = set()
            minSem += 1
            for node in nodes_with_0_indeg:
                for child in graph[node]:
                    indeg[child] -= 1
                    if indeg[child] == 0:
                        new_num_nodes_covered.add(child)
                num_nodes_covered += 1
            nodes_with_0_indeg = new_num_nodes_covered

        return minSem if num_nodes_covered == n else -1
