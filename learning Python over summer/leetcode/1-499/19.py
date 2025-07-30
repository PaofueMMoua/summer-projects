# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # make a variable to hold the listnode
        dummy_head = ListNode(0)
        # get the head of the node
        dummy_head.next = head

        fast = dummy_head
        slow = dummy_head

        for _ in range(n):
            fast = fast.next

        while fast.next is not None:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy_head.next