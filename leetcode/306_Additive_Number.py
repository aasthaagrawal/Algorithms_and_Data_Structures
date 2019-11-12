#https://leetcode.com/problems/additive-number/

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        if len(num)<3:
            return False
        self.lnum=len(num)
        self.num=num
        maxn1=self.lnum//2
        for i in range(maxn1):
            if i>0 and self.num[0]=="0":
                return False
            n1=int(self.num[:i+1])
            #print("n1: {}".format(n1))
            maxn2=(self.lnum-i-1)//2
            for j in range(i+1,i+1+maxn2):
                if (j-i-1>0 and self.num[i+1]=="0"):
                    break
                n2=int(self.num[i+1:j+1])
                #print("n2: {}".format(n2))
                pos=self.util(n1,n2,j+1)
                if pos:
                    return True
        return False
        
    def util(self,n1,n2,index):
        if index==self.lnum:
            return True
        pos=False
        i=index
        while i<self.lnum:
            if (i-index>0 and self.num[index]=="0"):
                    return False
            if n1+n2==int(self.num[index:i+1]):
                n3=int(self.num[index:i+1])
                pos=self.util(n2,n3,i+1)
                if pos:
                    return True
            elif n1+n2<int(self.num[index:i+1]):
                return False
            i+=1
	return False
