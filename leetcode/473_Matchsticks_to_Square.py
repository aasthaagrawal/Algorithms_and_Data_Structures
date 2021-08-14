#https://leetcode.com/problems/matchsticks-to-square/
#Time Complexity: O(nlogn + 4^n)

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        sum_matchsticks = sum(matchsticks)
        self.n = len(matchsticks)
        if self.n<4 or sum_matchsticks%4!=0:
            return False
        self.possible_each_side = sum_matchsticks/4
        self.matchsticks = sorted(matchsticks, reverse=True)
        self.res_arr = [0,0,0,0]
        
        return self.util(0)
    
    def util(self, i):
        if i==self.n:
            return (self.res_arr[0]==self.res_arr[1]==self.res_arr[2]==self.res_arr[3])
        
        for side in range(4):  
            if self.res_arr[side]+self.matchsticks[i] <= self.possible_each_side:
                self.res_arr[side]+=self.matchsticks[i]
                is_posible = self.util(i+1)
                if is_posible:
                    return True
                self.res_arr[side]-=self.matchsticks[i]

        return False
