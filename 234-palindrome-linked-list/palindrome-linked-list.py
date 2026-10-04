class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        lst = []
        current = head

        while current is not None:
            lst.append(current.val)
            current = current.next

        rev = lst[::-1]

        if lst == rev:
            return True
        else:
            return False