#https://leetcode.com/problems/asteroid-collision/
#Complexity: O(n) (Stack pushes and pops each element atmost once) 
#Space Complexity: O(n)

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        if len(asteroids)<=0:
            return []
        stack = []
        for a in asteroids:
            val = a
            while stack and val!=None and (stack[-1] > 0 and val < 0):
                if stack[-1] > abs(val):
                    val = None
                elif stack[-1] == abs(val):
                    stack.pop()
                    val = None
                else:
                    stack.pop()      
            if val:
                stack.append(val)
        
        return stack
