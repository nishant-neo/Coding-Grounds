/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
void sumNumbersUtil(TreeNode* A, int &sum, long long x) {
    if( A == NULL)
        return;
    x = x*10 + (A -> val);
    if( A -> left == NULL && A -> right == NULL){
        sum = (sum%1003 + x%1003)%1003;
        return;
    }
    sumNumbersUtil(A ->left, sum, x);
    sumNumbersUtil(A ->right, sum, x);
}
int Solution::sumNumbers(TreeNode* A) {
    int sum = 0;
    sumNumbersUtil(A, sum, 0);
    return sum;

}
