#https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result=[]*numRows
        for i in range(numRows):
            if i==0:
                result.append([1])
            else:
                resultIRow=[]*(i+1)
                for j in range(0,i+1):
                    if j==0 or j==i:
                        resultIRow.append(1)
                    else:
                        resultIRow.append(result[i-1][j-1]+result[i-1][j])
                result.append(resultIRow)
        return result
