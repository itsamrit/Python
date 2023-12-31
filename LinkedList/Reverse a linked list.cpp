    ListNode* reverseList(ListNode* head) {
        ListNode *cur=head,*next=NULL, *prev = NULL;
        while (cur) {
            next = cur->next;    //next
            cur->next = prev;    //cur->next
            prev = cur;          //prev
            cur = next;          //cur next
        }
        return prev;
    }
    // cur occurs in after a gap in sequence
