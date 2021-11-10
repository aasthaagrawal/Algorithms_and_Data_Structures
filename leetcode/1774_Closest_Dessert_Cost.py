#https://leetcode.com/problems/closest-dessert-cost/
#Time Complexity: O(n + 3^m)

class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        self.toppingCosts = toppingCosts
        self.m = len(toppingCosts)
        self.toppingVariation = []
        self.getToppingVariation(0,0)
        closestDiff = float("inf")
        closestArr = []
        for base in baseCosts:
            for topping in self.toppingVariation:
                cost = base+topping
                diff = abs(cost-target)
                if diff<closestDiff:
                    closestDiff = diff
                    closestArr = [cost]
                elif diff == closestDiff:
                    closestArr.append(cost)
        return min(closestArr)

    def getToppingVariation(self,i,cost):
        if i==self.m:
            self.toppingVariation.append(cost)
            return
        self.getToppingVariation(i+1,cost)
        self.getToppingVariation(i+1,cost+self.toppingCosts[i])
        self.getToppingVariation(i+1,cost+2*self.toppingCosts[i])
