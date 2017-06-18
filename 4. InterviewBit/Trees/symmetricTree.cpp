/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

int isMirror( TreeNode* A, TreeNode* B){
    if( A == NULL && B == NULL)
        return 1;
    if( A == NULL || B == NULL)
        return 0;
    return (A -> val == B -> val) && isMirror( A -> left, B -> right) && isMirror( A -> right, B -> left);
}
int Solution::isSymmetric(TreeNode* A) {
    if( A == NULL)
        return 1;
    return isMirror( A->left, A->right);
}
