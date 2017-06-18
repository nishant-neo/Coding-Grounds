/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
ListNode* Solution::swapPairs(ListNode* A) {
    if( A == NULL || A -> next == NULL)
        return A;
    ListNode* head = new ListNode(-1);
    head -> next = A;
    ListNode* cur= A;
    ListNode* prev = head;
    while( cur && cur -> next ){
        ListNode* temp = cur -> next;
        cur -> next = cur -> next -> next;
        prev -> next = temp;
        temp -> next = cur;
        prev = cur;
        cur = cur -> next;
    }
    return head -> next;
}

