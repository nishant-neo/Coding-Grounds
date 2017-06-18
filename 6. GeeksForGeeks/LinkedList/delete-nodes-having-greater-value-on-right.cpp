/*

The structure of linked list is the following

struct Node
{
int data;
Node* next;
};

*/
Node *compute(Node *head)
{
    if( head == NULL || head -> next == NULL)
        return head;
    Node* c = head;
    Node* p = NULL;
    Node* n = c -> next;
    while( n){
        c -> next = p;
        p = c;
        c = n;
        n = n -> next;
    }
    c -> next = p;

    int maxSoFar = c -> data;
    Node* temp = c -> next;
    Node* start = new Node();
    Node* t = start;
    t -> next = c;
    t = t -> next;
    while( temp ){
        if( temp -> data < maxSoFar);
        else{
            t -> next = temp;
            t = t -> next;
            maxSoFar = temp -> data;
        }
        temp = temp -> next;
    }
    t -> next = NULL;

    c = start -> next;
    p = NULL;
    n = c -> next;
    while( n){
        c -> next = p;
        p = c;
        c = n;
        n = n -> next;
    }
    c -> next = p;
    return c;
}
