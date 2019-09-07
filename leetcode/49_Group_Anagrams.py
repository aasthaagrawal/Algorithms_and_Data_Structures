#https://leetcode.com/problems/group-anagrams/
#Complexity:

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict={}
        for i in range(len(strs)):
            tmpStr=''.join(sorted(strs[i]))
            if tmpStr in dict:
                dict[tmpStr].append(strs[i])
            else:
                dict[tmpStr]=[strs[i]]
        result=[]
        for i in dict:
            result.append(dict[i])
        return result
