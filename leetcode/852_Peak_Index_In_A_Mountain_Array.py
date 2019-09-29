#https://leetcode.com/problems/peak-index-in-a-mountain-array/
#Complexity:O(log n)

class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        h=len(A)-1
        l=0
        while l<=h:
            m=l+int((h-l)/2)
            if A[m-1]<A[m] and A[m]>A[m+1]:
                return m
            elif A[m]<A[m+1]:
                l=m+1
            else:
                h=m-1
