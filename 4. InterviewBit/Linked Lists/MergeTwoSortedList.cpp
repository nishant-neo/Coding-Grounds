/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
ListNode* Solution::mergeTwoLists(ListNode* A, ListNode* B) {

    ListNode* t1 = A;
    ListNode* t2 = B;
    ListNode* t3;
    ListNode* C = NULL;
    while( t1 != NULL && t2 != NULL ){
        //cout<<t1->val<<" "<<t2->val<<endl;
        if( t1 -> val <= t2 -> val){
            if( C == NULL){
                C = A;
                t3 = C;
                t1 = t1 -> next;
            }
            else{
                //cout<<t3->val<<endl;
                t3 -> next = t1;
                t1 = t1 -> next;
                t3 = t3 -> next;
            }
        }
        else if( t2 -> val < t1 -> val){
            if( C == NULL){
                C = B;
                t3 = C;
                t2 = t2 -> next;
            }
            else{
                t3 -> next = t2;
                t2 = t2 -> next;
                t3 = t3 -> next;
            }
        }
    }
    if( t1 != NULL)
        t3 -> next = t1;
    else if( t2 != NULL)
        t3 -> next = t2;
    return C;

}


