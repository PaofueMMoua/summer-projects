# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

# set a base / get the head / a dummy
        dummy = ListNode(0, head)
        previous = dummy
        current = head
        while current:
            dupe = False
            while current.next and current.val == current.next.val:
                current = current.next
                dupe = True
            if dupe:
                previous.next = current.next
            else:
                previous = previous.next
            current = current.next
        return dummy.next
# find all nodes aka cycle through each node
# add each distinct node into a list
# remove anything that repeats again 





# Given the head of a sorted linked list, 
# delete all nodes that have duplicate numbers, 
# leaving only distinct numbers from the original list. 
# Return the linked list sorted as well