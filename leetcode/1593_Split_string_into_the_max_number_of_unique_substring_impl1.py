#https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/
#Time Complexity: O(2^n)

class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        self.n = len(s)
        self.result = 0
        self.s = s
        self.util(0,0,[])
        return self.result

    def util(self, cur_ind, cur_substr_start,l):
        if cur_ind == self.n:
            n_l = len(l)
            if n_l == len(set(l)) and self.result < n_l:
                self.result = n_l
            return
        self.util(cur_ind+1, cur_substr_start, l)
        l.append(self.s[cur_substr_start:cur_ind+1])
        self.util(cur_ind+1, cur_ind+1, l)
        l.pop()
