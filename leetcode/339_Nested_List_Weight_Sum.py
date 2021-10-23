#https://leetcode.com/problems/nested-list-weight-sum/

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        return self.util(nestedList, 1)

    def util(self, l, depth):
        result = 0
        for ele in l:
            if ele.isInteger():
                result += (depth*ele.getInteger())
            else:
                result += self.util(ele.getList(),depth+1)
        return result
