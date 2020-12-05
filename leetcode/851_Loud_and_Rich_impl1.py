#https://leetcode.com/problems/loud-and-rich/
#Complexity:
#map function has complexity O(N)
#richer_graph construction has complexity of O(len(richer)) which in worst case can be N^2
#Overall complexity is O(N^2)

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        N = len(quiet)
        self.output = [-1]*N
        self.quiet = quiet
        self.richer_graph = [[] for _ in range(N)]
        
        for i in richer:
            self.richer_graph[i[1]].append(i[0])
        
        return map(self.auxFunc, range(N))
    
    def auxFunc(self, index):
        if self.output[index] == -1:
            self.output[index] = index
            for i in self.richer_graph[index]:
                res = self.output[i]
                if res == -1:
                    res = self.auxFunc(i)
                if self.quiet[res] < self.quiet[self.output[index]]:
                    self.output[index] = res
        return self.output[index]
