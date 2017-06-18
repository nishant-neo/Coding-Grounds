/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
ListNode* Solution::reorderList(ListNode* A) {
    int n = 0;
    ListNode* cur = A;
    while(cur){
        n++;
        cur = cur -> next;
    }
    if( n <= 2)
        return A;
    ListNode* slow = A;
    ListNode* fast = A;
    ListNode* prev = NULL;
    while( slow != NULL && fast != NULL && fast->next != NULL && fast->next->next != NULL){
        prev = slow;
        slow = slow -> next;
        fast = fast -> next -> next;
    }
    prev = NULL;
    cur = slow -> next;
    slow -> next = NULL;
    ListNode* fr = cur -> next;
    while( fr){
        cur -> next = prev;
        prev = cur;
        cur = fr;
        fr = cur -> next;
    }
    cur -> next = prev;
    ListNode * temp = A;
    ListNode* head = new ListNode(-1);
    ListNode* t = head;
    ListNode* l = cur;
    while( l && temp){
        t ->  next = temp;
        temp = temp -> next;
        t = t -> next;

        t -> next = l;
        l = l -> next;
        t = t -> next;
    }
    if( l )
        t -> next = l;
    else if( temp)
        t -> next = temp;
    return head-> next;

}
