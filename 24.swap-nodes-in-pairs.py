#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        newHead=head.next

        prev=None 
        curr=head

        while curr and curr.next:
            temp=curr.next
            
        # third=head.next.next
        # temp=head

        # head=head.next
        # head.next=temp
        # temp.next=self.swapPairs(third)
        # return head

        
# @lc code=end

