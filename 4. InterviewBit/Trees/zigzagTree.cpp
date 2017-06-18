/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
vector<vector<int> > Solution::zigzagLevelOrder(TreeNode* A) {
    vector<vector<int> > res;
    if( A == NULL)
        return res;
    vector<int> row;
    stack<TreeNode*> current;
    stack<TreeNode*> next;
    current.push( A);
    int flag = 1;
    while( !current.empty()){
        TreeNode* temp = current.top(); current.pop();
        if( temp ){
            row.push_back(temp->val);
            //cout<<temp->val<<" ";
            if( flag ){
                if( temp -> left) next.push(temp -> left);
                if( temp -> right) next.push(temp -> right);
            }
            else{
                if( temp -> right) next.push(temp -> right);
                if( temp -> left) next.push(temp -> left);
            }
        }

        if( current.empty()){
            //cout<<endl;
            res.push_back(row);
            row.clear();
            flag = 1 - flag;
            next.swap(current);
        }
    }
    //cout<<res.size()<<endl;
    return res;

}
