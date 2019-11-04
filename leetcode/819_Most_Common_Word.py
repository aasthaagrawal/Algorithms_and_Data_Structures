#https://leetcode.com/problems/most-common-word/

import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph=paragraph.lower()
        pattern='[a-zA-Z]+'
        l=re.findall(pattern,paragraph)
        d={}
        result_string=""
        result_max=-float("inf")
        b={}
        for i in banned:
            b[i]=1
        for i in range(len(l)):
            if l[i] not in b:
                print(l[i])
                if l[i] in d:
                    d[l[i]]+=1
                else:
                    d[l[i]]=1
                if d[l[i]]>result_max:
                    result_max=d[l[i]]
                    result_string=l[i]
        return result_string
      
