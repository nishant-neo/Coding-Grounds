/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
ListNode* Solution::addTwoNumbers(ListNode* A, ListNode* B) {
    ListNode* t1 = A;
    ListNode* t2 = B;
    ListNode* C = new ListNode(-1);
    ListNode* t3 = C;
    int carry = 0;
    while( t1 || t2)
    {
        int x = t1 ? t1->val : 0;
        int y = t2 ? t2->val : 0;
        int v = (x + y + carry);
        ListNode* temp = new ListNode(v % 10);
        carry = v / 10;
        t3 -> next = temp;
        t3 = t3 -> next;
        t2 = t2 ? t2->next : t2;
        t1 = t1 ? t1->next : t1;
    }
    if( carry != 0){
        ListNode* temp = new ListNode(carry);
        t3 -> next = temp;
        t3 -> next -> next = NULL;
    }
    return C->next;
}
