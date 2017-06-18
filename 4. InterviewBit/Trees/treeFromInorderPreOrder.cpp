/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

int find(vector<int> &inorder, int l, int r, int val ){
    for( ; l <= r; l++){
        if( inorder[l] == val)
            return l;
    }
}
TreeNode* buildTreeUtil(vector<int> &preorder, vector<int> &inorder, int l, int r, int &k) {
    if( l > r)
        return NULL;
    TreeNode* root = new TreeNode(preorder[k]);
    k++;

    int m = find( inorder, l, r, root->val);
    root -> left = buildTreeUtil(preorder, inorder, l, m-1, k);
    root -> right = buildTreeUtil(preorder, inorder, m+1, r, k);
    return root;
}
TreeNode* Solution::buildTree(vector<int> &preorder, vector<int> &inorder) {
    if( preorder.size() == 0 && inorder.size() == 0)
        return NULL;
    int k = 0;
    return buildTreeUtil(preorder, inorder, 0, inorder.size()-1, k);
}
