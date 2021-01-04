#https://leetcode.com/problems/reorganize-string/
#Time Complexity: O(A(N+log A)) where N is the length of string and A is the size of alphabets in given string
#Space Complexity: O(A+N)

class Solution:
    def reorganizeString(self, S: str) -> str:
        d = {}
        for ch in set(S):
            d[ch] = S.count(ch)
        A = []
        N = len(S)
        for key, val in sorted(d.items(), key=lambda item: item[1]):
            if val > (N+1)//2:
                return ""
            else:
                A.extend(key*val)
        res = [None]*N
        res[1::2], res[::2] = A[:N//2], A[N//2:]
        return "".join(res)
