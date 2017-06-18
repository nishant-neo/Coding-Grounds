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
    ListNode* prevprev = NULL;
    ListNode* cur = prev -> next;
    ListNode* start = prev;
    //cout<<"here"<<endl;
    while( cur != NULL){
       //cout<<prev->val<<" "<<cur->val<<endl;
       while( cur -> next != NULL && cur -> next -> val == prev -> val)
                cur = cur ->  next;
            cur = cur -> next;
        if( cur -> val != prev -> val){
            prev -> next = cur;
            prevprev = prev;
            prev = cur;
            cur = cur -> next;
        }
        else{


            if( prevprev == NULL){
                prev = cur;
                start = prev;
                if( cur == NULL)
                    break;
                cur = cur -> next;
            }else{
                prev = prevprev;
                prev -> next = cur;
            }
        }
    }
    return start;
}
