#https://leetcode.com/problems/median-of-two-sorted-arrays/
#Time Complexity: O(log m) where m and n are sizes of nums1 and nums2 and m<n

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        size1 = len(nums1)
        size2 = len(nums2)
        if size2 < size1:
            nums1, nums2 = nums2, nums1
            size1, size2 = size2, size1

        l, r = 0, size1-1
        total = size1 + size2
        half = (total+1) // 2
        while True:
            if l<= r:
                m = l + (r-l)//2
            else:
                m = -1
            m2 = half - (m+1) - 1
            l1 = nums1[m] if m >= 0 else -float("inf")
            r1 = nums1[m+1] if m+1<size1 else float("inf")
            l2 = nums2[m2] if m2 >= 0 else -float("inf")
            r2 = nums2[m2+1] if m2+1<size2 else float("inf")
            if l1 > r2:
                r = m - 1
            elif l2 > r1:
                l = m + 1
            else:
                if total % 2 == 1:
                    return max(l1,l2)
                else:
                    return ( min(r1,r2) + max(l1,l2))/2
