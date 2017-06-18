/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
int findRoot(vector<int> &inorder, int l, int r, int val  ){
    /*while( l <= r ){
        int mid = l + (r-l)/2;
        if( inorder[mid] == val)
            return mid;
        else if( inorder[mid] < val)
            l = mid+1;
        else
            r = mid-1;
    }*/
    //cout<<"FF\n";
    int i;
    for (i = l; i <= r; i++)
    {
        if (inorder[i] == val)
            break;
    }
    return i;

}
TreeNode* buildTreeUtil( vector<int> &inorder, vector<int> &postorder, int l, int r, int *k ){
    if( l > r)
        return NULL;
    //cout<<"GG"<<endl;
    TreeNode* root = new TreeNode(postorder[*k]);
    (*k)--;
    int m = findRoot( inorder, l, r, root->val);

    root -> right = buildTreeUtil( inorder, postorder, m+1, r, k );
    root -> left = buildTreeUtil( inorder, postorder, l, m-1, k);
    return root;
}
TreeNode* Solution::buildTree(vector<int> &inorder, vector<int> &postorder) {

    if( inorder.size() == 0 && postorder.size() == 0)
        return NULL;
    int k = inorder.size()-1;
    return buildTreeUtil( inorder, postorder, 0, inorder.size()-1, &k );
}
