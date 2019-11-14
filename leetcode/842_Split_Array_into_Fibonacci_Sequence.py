#https://leetcode.com/problems/split-array-into-fibonacci-sequence/

class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        self.result=[]
        if len(S)<3:
            return self.result
        self.n=len(S)
        self.S=S
        n1n2len=2*self.n//3
        for i in range(n1n2len):
            if i>0 and self.S[0]=='0':
                return self.result
            n1=int(self.S[:i+1])
            if n1>(2**31-1):
                return self.result
            for j in range(i+1,n1n2len+1):
                if (j-i==1) or (j-i>1 and self.S[i+1]!='0'):
                    n2=int(self.S[i+1:j+1])
                    if n2>(2**31-1):
                        continue
                    res=self.util(j+1,n1,n2)
                    if res==True:
                        self.result.append(n2)
                        self.result.append(n1)
                        return self.result[::-1]
        return self.result
        
    def util(self,index,n1,n2):
        if index==self.n:
            return True
        for i in range(index+1,self.n+1):
            if i-index>1 and self.S[index]=='0':
                return False
            n3=int(self.S[index:i])
            if n3>(2**31-1):
                    return False
            if n1+n2==n3:
                res=self.util(i,n2,n3)
                if res==True:
                    self.result.append(n3)
                    return True
            elif n1+n2<n3:
                return False
        return False
