from typing import Optional
class Solution:
    def reverseList(self, head:Optional[ListNode]) -> [ListNode]:
        prev,curr= None, head

        while curr:
            temp = curr.next
            curr.next =prev
            prev = curr
            curr = temp
        return prev