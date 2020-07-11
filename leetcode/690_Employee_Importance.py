#https://leetcode.com/problems/employee-importance/
#Complexity: O(V+E)
"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employees_hm = {employee.id: [employee.importance, employee.subordinates] for employee in employees}
        curr_level = [id]
        next_level = []
        importance = 0
        while len(curr_level) > 0:
            for id in curr_level:
                employee = employees_hm[id]
                importance += employee[0]
                next_level.extend(employee[1])
            curr_level = next_level
            next_level = []
        return importance
        
