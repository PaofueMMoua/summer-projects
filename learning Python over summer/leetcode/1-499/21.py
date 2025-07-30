# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # use a dummy to simplify listNode
        dummy = ListNode(0)
        current = dummy
# only loop while list1 and list2 contain something
        while list1 and list2:
            #check if the value of list1 is less than the value of list2
            if list1.val < list2.val:
# change the current next to be equal to list1 and then change list1 to the next on in the instance.
                current.next = list1
                list1 = list1.next
            else:
# set the next thing to list2 instead and then make the next list2 to the next one.
                current.next = list2
                list2 = list2.next
# set the current equal to the next one aka the empty one
            current = current.next
#change the current next equal to list1 if list1 contains things else itll be list2. this is for the chance that one list is longer than the other.
        current.next = list1 if list1 else list2
# returning the dummy
        return dummy.next