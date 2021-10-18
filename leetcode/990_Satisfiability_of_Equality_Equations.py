#https://leetcode.com/problems/satisfiability-of-equality-equations/
#Space Complexity: O(m) where m is the number of variables (which in worst case would be 2n)
#Time Complexity: O(nm) where n is the length of equations and m is the number of variables. If m=2n, then time complexity would be O(n^2)

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        all_vars = set()
        for eq in equations:
            all_vars.add(eq[0])
            all_vars.add(eq[-1])

        self.class_dict = {}
        i = 0
        for var in all_vars:
            self.class_dict[var] = i
            i += 1

        for eq in equations:
            if eq[1:3] == "==":
                self.union(self.class_dict[eq[0]],self.class_dict[eq[-1]])
        for eq in equations:
            if eq[1:3] == "!=":
                if self.class_dict[eq[0]] == self.class_dict[eq[-1]]:
                    return False
        return True

    def union(self, class1, class2):
        new_class = class1 if class1<class2 else class2
        old_class = class1 if class1>=class2 else class2
        for key,value in self.class_dict.items():
            if value==old_class:
                self.class_dict[key]=new_class
