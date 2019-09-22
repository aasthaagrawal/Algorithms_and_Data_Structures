#https://leetcode.com/problems/ones-and-zeroes/
#Complexity: O(snm) where s in the number of strings

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dpAux=[[0 for j in range(n+1)] for i in range(m+1)]
        
        for s in strs:
            num_m,num_n=s.count("0"),s.count("1")
            for i in reversed(range(num_m,m+1)):
                for j in reversed(range(num_n,n+1)):
                    dpAux[i][j]=max(dpAux[i][j],dpAux[i-num_m][j-num_n]+1)
        print(dpAux)
        return dpAux[m][n]
