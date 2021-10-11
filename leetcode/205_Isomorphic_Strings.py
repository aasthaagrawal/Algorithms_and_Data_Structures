#https://leetcode.com/problems/isomorphic-strings/
#Time Complexity: O(n)
#Space Complexity: O(n)

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ns = len(s)
        nt = len(t)
        if ns!=nt:
            return False
        
        org_to_dest = {}
        dest_to_org = {}
        
        for index in range(ns):
            if (s[index] in org_to_dest and org_to_dest[s[index]]!=t[index]) or (t[index] in dest_to_org and dest_to_org[t[index]] != s[index]):
                    return False
            else:
                org_to_dest[s[index]] = t[index]
                dest_to_org[t[index]] = s[index]
        
        return True
