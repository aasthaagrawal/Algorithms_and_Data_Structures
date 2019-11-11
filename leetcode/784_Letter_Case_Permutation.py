#https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        if len(S)==0:
            return []
        self.result=[]
        self.util(S,0,len(S))
        return self.result
        
    def util(self,substr,index,n):
        if index==n:
            self.result.append(substr[:])
            return
        if substr[index].isupper():
            self.util(substr,index+1,n)
            substr=substr[:index]+chr(ord(substr[index])+32)+substr[index+1:]
            self.util(substr,index+1,n)
            substr=substr[:index]+chr(ord(substr[index])-32)+substr[index+1:]
        elif substr[index].islower():
            self.util(substr,index+1,n)
            substr=substr[:index]+chr(ord(substr[index])-32)+substr[index+1:]
            self.util(substr,index+1,n)
            substr=substr[:index]+chr(ord(substr[index])+32)+substr[index+1:]
        else:
            self.util(substr,index+1,n)
