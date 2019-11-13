#https://leetcode.com/problems/gray-code/

class Solution:
    def grayCode(self, n: int) -> List[int]:
        self.multiplier=[2**i for i in range(n-1,-1,-1)]
        self.result=[]
        self.resset=set()
        self.resset.add(0)
        self.result.append(0)
        s=['0' for i in range(n)]
        self.createsubstr(''.join(s),n)
        return self.result
        
    def toggle(self,ch):
        if ch=='1':
            return '0'
        if ch=='0':
            return '1'
    def stonum(self,s,n):
        num=0
        for i in range(n):
            num+=(int(s[i])*self.multiplier[i])
        return num
        
    def createsubstr(self,s,n):
        i=0
        while i<n:
            s=s[:i]+self.toggle(s[i])+s[i+1:]
            num=self.stonum(s,n)
            if num not in self.resset:
                #print(num)
                self.resset.add(num)
                self.result.append(num)
                self.createsubstr(s[:],n)
                break
            else:
                s=s[:i]+self.toggle(s[i])+s[i+1:] 
            i+=1
