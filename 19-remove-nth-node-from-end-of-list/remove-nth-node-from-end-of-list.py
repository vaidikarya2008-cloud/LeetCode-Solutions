class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        lst = []
        current = head

        while current is not None:
            lst.append(current)
            current = current.next

        index = len(lst) - n

        if index == 0:
            return head.next

        target = lst[index]
        current = head

        while current.next is not None:
            if current.next == target:
                current.next = current.next.next
                break
            current = current.next

        return head