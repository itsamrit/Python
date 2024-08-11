def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    cur = None
    while(head):
        head.next, cur, head = cur, head, head.next
    
    return cur
