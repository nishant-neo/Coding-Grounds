/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
vector<int> Solution::inorderTraversal(TreeNode* A) {
    vector <int> res;
    stack <TreeNode*> st;
    if( A == NULL)
        return res;
    while(1){
        while( A ){
            st.push(A);
            A = A -> left;
        }
        if( st.empty())
            return res;
        A = st.top(); st.pop();
        res.push_back(A->val);
        A = A -> right;
    }
}
