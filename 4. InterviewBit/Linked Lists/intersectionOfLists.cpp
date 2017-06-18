/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
int lengthList( ListNode* A)
{
    int m = 0;
    ListNode* temp = A;
    while( temp != NULL){
        temp = temp -> next;
        m++;
    }
    return m;
}
ListNode* Solution::getIntersectionNode(ListNode* A, ListNode* B) {
    if( A == NULL || B == NULL)
        return NULL;
    int m = lengthList(A);
    int n = lengthList(B);
    //cout<<m << " "<<n<<endl;
    int it = abs(m-n);
    if( m > n){
        while( it--)
            A = A -> next;
    }
    else{
        while( it--)
            B = B -> next;
    }

    while( A != NULL && B != NULL){
        //cout<< A->val<< " "<<B->val<<endl;
        if( A  == B )
            return A;
        A = A -> next;
        B = B -> next;
    }
    return NULL;

}

