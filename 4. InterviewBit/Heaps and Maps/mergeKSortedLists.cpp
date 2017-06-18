/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

struct compare {
    bool operator()(ListNode* const & p1, ListNode* const & p2) {
    // return "true" if "p1" is ordered before "p2", for example:
        return p1->val > p2->val;
    }
};
ListNode* Solution::mergeKLists(vector<ListNode*> &A) {
    ListNode* head = new ListNode(0);
    ListNode* cur = head;
    int k = A.size();
    priority_queue <ListNode*, vector<ListNode*>, compare> minheap;
    for( int i = 0; i < k; i++){
        minheap.push( A[i]);
    }
    while( !minheap.empty()){
        cur -> next = minheap.top();
        minheap.pop();
        cur = cur -> next;
        if( cur -> next)
            minheap.push(cur-> next);
    }
    cur -> next =  NULL;
    return head -> next;

}
