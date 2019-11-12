#https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.edges={}
        for p in prerequisites:
            if p[0] in self.edges:
                self.edges[p[0]].append(p[1])
            else:
                self.edges[p[0]]=[p[1]]
        visited=[False]*(numCourses)
        self.recstack=[False]*(numCourses)
        for c in range(numCourses):
            if visited[c]==False:
                r=self.util(c,visited)
                if r==False:
                    return False
        return True
        
    def util(self,c,visited):
        visited[c]=True
        self.recstack[c]=True
        if c in self.edges:
            for v in self.edges[c]:
                if self.recstack[v]==True:
                    return False
                if visited[v]==False:
                    p=self.util(v,visited)
                    if p==False:
                        return False
        self.recstack[c]=False
        return True
