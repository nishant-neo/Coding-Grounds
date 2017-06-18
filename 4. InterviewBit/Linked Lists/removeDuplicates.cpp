/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
ListNode* Solution::deleteDuplicates(ListNode* A) {
    if( A == NULL || A -> next == NULL)
        return A;
    ListNode* prev = A;
    ListNode* cur = A -> next;
    while( cur != NULL){
        if( prev -> val == cur -> val);
        else {
            prev -> next = cur;
            prev = cur;
        }
        cur = cur -> next;
    }
    prev -> next = NULL;
    return A;
}

