#https://leetcode.com/problems/couples-holding-hands/
#Time complexity: O(n)
#Space Complexity: O(n)

class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        d = {}
        for i,val in enumerate(row):
            d[val] = i
        swaps = 0
        n = len(row)//2
        for i in range(n):
            index = 2*i
            if row[index]//2 != row[index+1]//2:
                swaps += 1
                partner = None
                if row[index] %2 == 0:
                    partner = row[index]+1
                else:
                    partner = row[index] - 1
                row[d[partner]] = row[index+1]
                d[row[index+1]] = d[partner]
                row[index+1] = partner
                d[partner] = index + 1
        return swaps

