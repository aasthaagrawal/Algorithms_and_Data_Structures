#https://leetcode.com/problems/minimum-window-substring/
#Space Complexity: O(n) where n is the length of t; Plus the length of resultSubstring which could max be O(m)
#Time Complexity: O(m+mn)= O(mn)

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        if m < len(t):
            return ""
        self.processedT = {}
        for ch in t:
            if ch in self.processedT:
                self.processedT[ch] += 1
            else:
                self.processedT[ch] = 1

        left = 0
        right = 0
        isRight = True
        result = float("inf")
        resultString = ""
        while right < m:
            if isRight:
                if s[right] in self.processedT:
                    self.processedT[s[right]] -= 1
                if self.isValid():
                    isRight = False
                    l = right - left + 1
                    if l<result:
                        result = l
                        resultString = s[left:right+1]
                else:
                    right += 1
            else:
                if s[left] in self.processedT:
                    self.processedT[s[left]] += 1
                left += 1
                if self.isValid():
                    l = right - left + 1
                    if l<result:
                        result = l
                        resultString = s[left:right+1]
                else:
                    isRight = True
                    right += 1

        return resultString

    def isValid(self):
        for value in self.processedT.values():
            if value>0:
                return False
        return True
