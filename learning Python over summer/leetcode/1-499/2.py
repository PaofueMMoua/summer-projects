# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2 ):
        # get both list
        # make a for loop to loop through the first list and get each thing in the list
        current_node = l1
        temp_node = l2
        while(current_node):
            l1.val = l1.val + l2.val
            if l1.next.val == '':
                current_node = False
            l2.next
            l1.next
        return l1
        # make the list an integer list
        # add the points of list 1 and the points of list 2 together as they come up using the index of the points
        #  

l1 = [2,4,3]
l2 = [5,6,4]
print()
print()
print(Solution().addTwoNumbers(l1, l2))