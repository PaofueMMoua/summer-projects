class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        curr = head

        while curr:
            has_duplicate = False
            while curr.next and curr.val == curr.next.val:
                curr = curr.next
                has_duplicate = True

            if has_duplicate:
                prev.next = curr.next
            else:
                prev = prev.next

            curr = curr.next

        return dummy.next