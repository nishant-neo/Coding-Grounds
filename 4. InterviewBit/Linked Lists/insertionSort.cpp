/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
ListNode* Solution::insertionSortList(ListNode* A) {
    ListNode* start = A;
    ListNode* cur = A -> next;
    ListNode* end = A;
    ListNode* t1 = start;
    ListNode* prev = NULL;
    while( cur ){
        t1 = start;
        while( t1  != end && cur -> val > t1 -> val ){
            prev = t1;
            t1 = t1 -> next;
        }
        if( t1 == start && t1 -> val > cur -> val){
            ListNode* temp = cur;
            cur = cur -> next;
            temp -> next = start;
            start = temp;
            end->next =NULL;
        }
        else if( t1 -> val > cur -> val){
            ListNode* temp = cur;
            cur = cur -> next;
            prev -> next = temp;
            temp -> next = t1;
            end->next =NULL;

        }
        else{
            t1 -> next = cur;
            end = cur;
            cur = cur -> next;
            end -> next = NULL;
        }
        /*t1 = start;
        //while( t1 != end){
            cout<<t1->val<<" ";
            t1 = t1 -> next;
        }
        cout<<end->val;
        cout<<endl;*/
    }
    return start;

}

