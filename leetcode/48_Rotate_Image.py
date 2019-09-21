#https://leetcode.com/problems/rotate-image/
#Complexity(O(n^2))

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        leftIndex=0
        rightIndex=len(matrix)-1
        iter=0
        while(leftIndex<rightIndex):
            for i in range(leftIndex,rightIndex):
                tmp=matrix[leftIndex][i]
                matrix[leftIndex][i]=matrix[rightIndex-i+iter][leftIndex]
                matrix[rightIndex-i+iter][leftIndex]=matrix[rightIndex][rightIndex-i+iter]
                matrix[rightIndex][rightIndex-i+iter]=matrix[i][rightIndex]
                matrix[i][rightIndex]=tmp
            leftIndex+=1
            rightIndex-=1
            iter+=1
