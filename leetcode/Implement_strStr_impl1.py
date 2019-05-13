#https://leetcode.com/problems/implement-strstr/
#Complexity O(needleLen*haystackLen)

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        result=-1
        needleLen=len(needle)
        haystackLen=len(haystack)
        
        if needle:
            for i in range(haystackLen-needleLen+1):
                result=i
                for j in range(needleLen):
                    if needle[j]!=haystack[i+j]:
                        result=-1
                        break
                if result!=-1:
                    break
        else:
            result=0
                   
        return result
