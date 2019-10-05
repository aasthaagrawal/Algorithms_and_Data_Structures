#https://leetcode.com/problems/keys-and-rooms/
#Complexity: O(n*keys)

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n=len(rooms)
        visited=[False]*n
        q=[]
        visited[0]=True
        for i in rooms[0]:
            q.append(i)
            visited[i]=True
        while len(q):
            ele=q.pop(0)
            for i in rooms[ele]:
                if not visited[i]:
                    q.append(i)
                    visited[i]=True
        for i in visited:
            if not i:
                return False
        return True
