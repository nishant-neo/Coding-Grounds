/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

int isBSTUtil( TreeNode* A, int min, int max)
{
    if( A == NULL)
        return 1;
    if( A -> val < min || A -> val > max)
        return 0;
    return isBSTUtil( A -> left, min, A->val -1 ) && isBSTUtil( A -> right, A ->val +1,  max);
}
int Solution::isValidBST(TreeNode* A) {
    return isBSTUtil( A, INT_MIN, INT_MAX);

}

