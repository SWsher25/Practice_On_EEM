class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        left = head
        right = head.next
        
        while right and right.next:
            left = left.next 
            right = right.next.next

        second = left.next
        prev = None
        left.next = None

        while second:
            nxt = second.next 
            second.next = prev 
            prev = second 
            second = nxt

        first = head
        second = prev

        while second:
            tmp1 = first.next 
            tmp2 = second.next 

            first.next = second 
            second.next = tmp1 

            first = tmp1 
            second = tmp2