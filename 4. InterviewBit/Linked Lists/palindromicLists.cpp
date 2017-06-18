/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
int Solution::lPalin(ListNode* A) {
    if( !A || !(A -> next) )
        return 1;
    string num = "";
    ListNode* temp = A;
    int n = 0;
    while( temp){
        n = n+1;
        temp = temp -> next;
    }
    int half = n / 2;
    temp = A;
    while( half-- ){
        temp = temp -> next;
    }
    if( n % 2 != 0)
        temp = temp -> next;

    ListNode *prev = NULL;
    ListNode *cur = temp;
    ListNode *next = cur -> next;

    while( next != NULL){
        cur -> next = prev;
        prev = cur;
        cur = next;
        next = cur -> next;
    }
    cur -> next = prev;

    ListNode* t1 = A;
    ListNode* t2 = cur;
    while( t1 && t2){
        if( t1 -> val != t2 -> val)
            return 0;
        t1 = t1 -> next;
        t2 = t2 -> next;
    }
    return 1;

}
