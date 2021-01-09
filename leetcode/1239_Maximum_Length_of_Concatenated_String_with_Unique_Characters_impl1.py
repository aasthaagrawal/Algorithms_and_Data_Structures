#https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
#Complexity: O(2^len(arr))

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        self.res = 0
        self.arr = arr
        self.len = len(arr)
        self.processSubstring(0, set(), 0)
        return self.res
    
    def processSubstring(self, ind, d, strLen):
        if ind == self.len:
            self.res = max(self.res, strLen)
            return
        #not include d
        self.processSubstring(ind+1, d, strLen)
        
        #include d
        d2 = set(self.arr[ind])
        if len(d2) != len(self.arr[ind]) or d2.intersection(d):
            return
        self.processSubstring(ind+1, d2.union(d), strLen+len(self.arr[ind]))
