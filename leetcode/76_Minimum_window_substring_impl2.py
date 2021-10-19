#https://leetcode.com/problems/minimum-window-substring/submissions/
#Space Complexity: O(n)
#Time Complexity: O(n + m^2)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        if m < len(t):
            return ""
        t_dict = {}
        for ch in t:
            if ch in t_dict:
                t_dict[ch] += 1
            else:
                t_dict[ch] = 1
        distinct_count = len(t_dict)

        left = 0
        result = float("inf")
        res_l = -1
        for i,ch in enumerate(s):
            if ch in t_dict:
                t_dict[ch] -= 1
                if t_dict[ch] == 0:
                    distinct_count -= 1
            while distinct_count==0:
                if result > i-left+1:
                    result = i-left+1
                    res_l = left
                if s[left] in t_dict:
                    t_dict[s[left]] += 1
                    if t_dict[s[left]] > 0:
                        distinct_count += 1
                left += 1

        if res_l==-1:
            return ""
        res_r = res_l+result
        return s[res_l:res_r]
