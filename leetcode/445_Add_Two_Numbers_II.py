#https://leetcode.com/problems/add-two-numbers-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1=[]
        s2=[]
        l=l1
        while l:
            s1.append(l.val)
            l=l.next
        l=l2
        while l:
            s2.append(l.val)
            l=l.next
        carry=0
        res=None
        while len(s2)>0 and len(s1)>0:
            val=s2.pop(-1)+s1.pop(-1)+carry
            carry=int(val/10)
            val=val%10
            newres=ListNode(val)
            newres.next=res
            res=newres
        while len(s2)>0:
            val=s2.pop(-1)+carry
            carry=int(val/10)
            val=val%10
            newres=ListNode(val)
            newres.next=res
            res=newres
        while len(s1)>0:
            val=s1.pop(-1)+carry
            carry=int(val/10)
            val=val%10
            newres=ListNode(val)
            newres.next=res
            res=newres
        if carry>0:
            newres=ListNode(carry)
            newres.next=res
            res=newres
        return res
