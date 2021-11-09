#https://leetcode.com/problems/ambiguous-coordinates/
#Time Complexity: O(n^3)

class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        self.result = []
        n = len(s)
        for i in range(2,n-1):
            num1 = s[1:i]
            num2 = s[i:n-1]
            for n1 in self.getAllNums(num1):
                for n2 in self.getAllNums(num2):
                    self.result.append("(" + n1 + ", " + n2 + ")")
        return self.result

    def getAllNums(self, numstring):
        l = len(numstring)
        if l==1:
            return [numstring]
        if numstring[0]=='0':
            if numstring[-1]=='0':
                return []
            return [numstring[0]+"."+numstring[1:]]
        if numstring[-1]=='0':
            return [numstring]
        res = [numstring]
        for i in range(1,l):
            res.append(numstring[:i]+"."+numstring[i:])
        return res

