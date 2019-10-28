#https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry=0
        head=None
        prev=None
        while(l1 or l2):
            sum=0
            if l1:
                sum+=l1.val
                l1=l1.next
            if l2:
                sum+=l2.val
                l2=l2.next
            sum+=carry
            v=sum%10
            carry=int(sum/10)
            node=ListNode(v)
            if head==None:
                head=node
                prev=node
            else:
                prev.next=node
                prev=node
        if carry>0:
            node=ListNode(carry)
            prev.next=node
        return head
        
