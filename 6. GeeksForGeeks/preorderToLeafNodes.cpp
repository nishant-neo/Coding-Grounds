#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
struct TreeNode{
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};
int findPos(vector <int> inorder, int val, int l, int r){
    while( l <= r){
        int mid = l + (r-l)/2;
        if( inorder[mid] == val)
            return mid;
        else if( inorder[mid] > val)
            r = mid-1;
        else
            l = mid+1;
    }
    return 0;
}
TreeNode* formTree( vector <int> inorder, vector <int> preorder, int l, int r, int &k){
    if( l > r)
        return NULL;
    int val = preorder[k];
    k++;
    TreeNode* root = new TreeNode(val);
    int pos = findPos(inorder, root->val,  l, r);
    root -> left = formTree( inorder, preorder, l, pos-1, k);
    root -> right = formTree( inorder, preorder, pos+1, r, k);
    return root;

}
void inorder( TreeNode* root){
    if( root == NULL)
        return;
    inorder( root -> left);
    if( !root -> left && !root -> right)
        cout<<root->val<<" ";
    inorder( root -> right);
}
int main()
{
    int t,n;
    cin>>t;
    while( t--){
        cin>>n;
        vector <int> pre(n);
        vector <int> in(n);
        for( int i = 0; i < n ; i++){
            cin>>pre[i];
            in[i] = pre[i];
        }
        sort( in.begin(), in.end());
        int k = 0;
        TreeNode* root = formTree( in, pre, 0, n-1, k);


        inorder( root);
        cout<<endl;
    }
	return 0;
}
