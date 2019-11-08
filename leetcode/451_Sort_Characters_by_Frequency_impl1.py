#https://leetcode.com/problems/sort-characters-by-frequency/

class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        sorted_d=sorted(d.items(),key=lambda x:x[1],reverse=True)
        l=[]
        for ele in sorted_d:
            l=l+[ele[0] for i in range(ele[1])]
        return ''.join(l)
