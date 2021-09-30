#https://leetcode.com/problems/kth-missing-positive-number/
#Complexity: O(log n)

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l = 0
        r = len(arr)
        
        def util(arr_val,arr_index):
            return arr_val - arr_index - 1
        
        while l<r:
            mid = l + (r-l)//2
            if util(arr[mid],mid)<k:
                l = mid+1
            else: 
                r = mid
        return l+k       
