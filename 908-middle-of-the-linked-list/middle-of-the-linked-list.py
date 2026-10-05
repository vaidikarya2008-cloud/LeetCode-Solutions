class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        lst = []
        current = head

        while current is not None:
            lst.append(current)
            current = current.next

        return lst[len(lst) // 2]