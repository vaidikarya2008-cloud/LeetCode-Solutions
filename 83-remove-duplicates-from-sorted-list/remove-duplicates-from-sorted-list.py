# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        check=[]

        current = head
        back = None

        while current is not None:
            if current.val in check:
                back.next = current.next
            else:
                check.append(current.val)
                back = current

            current = current.next

        return head