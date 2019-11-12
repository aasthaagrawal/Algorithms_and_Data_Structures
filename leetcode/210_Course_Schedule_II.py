#https://leetcode.com/problems/course-schedule-ii/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        self.edges={}
        for p in prerequisites:
            if p[1] in self.edges:
                self.edges[p[1]].append(p[0])
            else:
                self.edges[p[1]]=[p[0]]
        self.visited=[False]*(numCourses)
        self.stack=[]
        self.recstack=[False]*(numCourses)
        for c in range(numCourses):
            if self.visited[c]==False:
                r=self.util(c)
                if r==False:
                    return []
        return self.stack[::-1]
    
    def util(self,v):
        self.visited[v]=True
        self.recstack[v]=True
        if v in self.edges:
            for c in self.edges[v]:
                if self.recstack[c]==True:
                    return False
                if self.visited[c]==False:
                    p=self.util(c)
                    if p==False:
                        return False
        self.stack.append(v)
        self.recstack[v]=False
        return True
