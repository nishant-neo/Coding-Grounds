/*The node structure
struct Node {
int data;
Node * right, * left;
};*/

/*The function should return the root of the modified tree*/
Node* deleteNode(Node* root, int key)
{
    if( root == NULL)
        return NULL;

    Node* temp = root;

    if( root -> data > key){
        root -> left = deleteNode(root -> left, key);
        root -> right = NULL;
    }
    if( root -> data >= key){
        root = root -> left;
        temp -> left = NULL;
        free(temp);
        return root;
    }
    if( root -> data < key)
        root -> right = deleteNode(root -> right, key);
}

