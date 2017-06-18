/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
int findMax( vector<int> &A, int l, int r){
    int max = INT_MIN, in = -1;
    for( ; l<=r; l++){
        if( A[l] > max){
            max = A[l];
            in = l;
        }
    }
    return in;
}
TreeNode* buildTreeUtil( vector<int> &A, int l, int r ){
    if( l > r )
        return NULL;
    int in = findMax( A, l, r);
    TreeNode* root = new TreeNode(A[in]);
    root -> left = buildTreeUtil( A, l, in-1);
    root -> right = buildTreeUtil( A, in+1, r);
    return root;
}
TreeNode* Solution::buildTree(vector<int> &A) {
    return buildTreeUtil( A, 0, A.size()-1);
}

