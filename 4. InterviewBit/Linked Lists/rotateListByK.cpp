/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
ListNode* Solution::rotateRight(ListNode* A, int B) {
    int n = 0;
    ListNode* cur = A;
    ListNode* prev = NULL;
    while( cur){
        cur = cur -> next;
        n++;
    }
    B = B % n;
    if( B == 0)
        return A;
    cur = A;
    for( int i = 1; i < (n-B+1)&&  cur!= NULL; i++){
        prev = cur;
        cur = cur -> next;
    }
    ListNode *temp = cur;
    while( temp -> next )
        temp = temp -> next;
    temp -> next = A;
    prev -> next = NULL;
    return cur;
}
