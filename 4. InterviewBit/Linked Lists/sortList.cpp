/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
ListNode* merge( ListNode* A, ListNode* B ){
    ListNode* start = new ListNode(-1);
    ListNode* t1 = A;
    ListNode* t2 = B;
    ListNode* t3 = start;
    while( t1 && t2){
        if( t1 -> val <= t2 -> val){
            t3 -> next = t1;
            t1 = t1 -> next;
        }
        else{
            t3 -> next = t2;
            t2 = t2 -> next;
        }
        t3 = t3 -> next;
    }
    t3 -> next = t2 ? t2 : t1;
    return start -> next;

}
ListNode* Solution::sortList(ListNode* A) {
    if( A == NULL || A -> next == NULL)
        return A;
    ListNode* slow = A;
    ListNode* fast = A -> next;
    while( fast  && fast -> next ){
        slow = slow -> next;
        fast = fast -> next -> next;
    }
    fast = slow -> next;
    slow -> next = NULL;
    merge( sortList(A),  sortList(fast));
}
