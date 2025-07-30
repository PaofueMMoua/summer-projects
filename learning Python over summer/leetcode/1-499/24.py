# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # make a dummy
        dummy = ListNode(0)
        current = dummy
        # loop through while the node contains something
        while head:
        # set a new variable equal to the next node
            tempvar = head
            head = head.next
            head
        # swap the two nodes
        # return the ListNode 