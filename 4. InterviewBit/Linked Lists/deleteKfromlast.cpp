/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
ListNode* Solution::removeNthFromEnd(ListNode* A, int B) {
    ListNode* temp = A;
    ListNode* prev = NULL;
    int n =0;
    while( temp ){
        temp = temp -> next;
        n++;
    }
    temp=A;
    if(n <= B){
        A=A->next;
        free(temp);
        return A;
    }
    ListNode* head = new ListNode(-1);
    head -> next = A;
    ListNode* cur = head;
    for( int i = 0; i < (n - B + 1) && cur != NULL; i++){

        prev = cur;
        cur = cur -> next;
    }
    prev -> next = cur -> next;
    free(cur);
    return A ;
}

