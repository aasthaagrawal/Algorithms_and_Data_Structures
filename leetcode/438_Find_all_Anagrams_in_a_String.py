#https://leetcode.com/problems/find-all-anagrams-in-a-string/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pl=len(p)
        sl=len(s)
        if sl<pl:
            return []
        d={}
        for i in p:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        result=[]
        ds={}
        start=0
        for i in range(sl):
            if s[i] in ds:
                ds[s[i]]+=1
            else:
                ds[s[i]]=1
            if i-start+1>pl:
                ds[s[start]]-=1
                if ds[s[start]]==0:
                    del ds[s[start]]
                start+=1
            if i-start+1==pl:
                if ds==d:
                    result.append(start)
        return result
