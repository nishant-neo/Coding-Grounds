/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
ListNode* Solution::reverseList(ListNode* A) {
    if( A == NULL || A -> next == NULL)
        return A;
    ListNode* cur = A;
    ListNode* prev = NULL;
    ListNode* next = cur -> next;

    while( next != NULL ){
        cur -> next = prev;
        prev = cur;
        cur = next;
        next = cur -> next;
    }
    cur -> next = prev;
    return cur;
}

