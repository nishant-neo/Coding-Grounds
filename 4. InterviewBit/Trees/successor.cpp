/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
TreeNode* findMin( TreeNode* A){
    if( A == NULL)
        return NULL;
    TreeNode* temp = A;
    while( temp -> left ){
        temp = temp -> left;
    }
    return temp;

}
TreeNode* Solution::getSuccessor(TreeNode* A, int B) {
    if( A == nullptr )
        return NULL;
    TreeNode* temp = A;
    while( temp->val != B ){
        if( temp -> val > B)
            temp = temp -> left;
        else
            temp = temp -> right;
    }
    if( temp -> right )
        return findMin(temp->right);
    else{
        TreeNode* successor = NULL;
        TreeNode* ancestor = A;
        while( ancestor != temp){
            if( temp -> val < ancestor -> val){
                successor = ancestor;
                ancestor = ancestor -> left;
            }
            else
                ancestor = ancestor -> right;
        }
        return successor;
    }

}

