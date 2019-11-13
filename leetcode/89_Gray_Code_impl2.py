#https://leetcode.com/problems/gray-code/

class Solution:
    def grayCode(self, n: int) -> List[int]:
        self.result=[]
        self.generateGrayNum(0,n)
        return self.result
        
    def generateGrayNum(self,num,n):
        if n==0:
            self.result.append(num)
            return num
        num=self.generateGrayNum(num,n-1)
        num=num ^ (1<<(n-1))
        num=self.generateGrayNum(num,n-1)
        return num
