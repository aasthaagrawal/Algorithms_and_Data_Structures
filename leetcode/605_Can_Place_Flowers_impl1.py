#https://leetcode.com/problems/can-place-flowers/
#Complexity: O(n)
#Space complexity: O(1)

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n==0:
            return True
        count = 0
        num = len(flowerbed)
        for i in range(num):
            canPlant = False
            if flowerbed[i] == 0:
                canPlant = True
                if i!=0 and flowerbed[i-1]==1:
                    canPlant = False
                if canPlant and i!=(num-1) and flowerbed[i+1]==1:
                    canPlant = False
            if canPlant:
                flowerbed[i] = 1
                count += 1
                if count >= n:
                    return True
        return False
