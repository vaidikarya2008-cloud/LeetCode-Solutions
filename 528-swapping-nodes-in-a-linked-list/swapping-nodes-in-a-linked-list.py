# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        lst = []
        current = head

        while current is not None:
            lst.append(current)
            current = current.next

        first = lst[k - 1]
        last = lst[len(lst) - k]

        first.val, last.val = last.val, first.val

        return head