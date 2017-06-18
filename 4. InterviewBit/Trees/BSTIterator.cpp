/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
TreeNode* temp;
stack <TreeNode*> st;
BSTIterator::BSTIterator(TreeNode *root) {
    temp = root;
    while(!st.empty())
        st.pop();
}

/** @return whether we have a next smallest number */
bool BSTIterator::hasNext() {
    if( temp || !st.empty() )
        return true;
    else
        return false;
}

/** @return the next smallest number */
int BSTIterator::next() {
    int flag = 0;
    int res;
    while( flag == 0){
        if( temp != NULL){
            st.push(temp);
            temp = temp -> left;
        }
        else{
            if( st.empty())
                flag = 1;
            else{
                temp = st.top(); st.pop();
                res = temp -> val;
                temp = temp -> right;
                flag = 1;
            }
        }
    }
    return res;
}

/**
 * Your BSTIterator will be called like this:
 * BSTIterator i = BSTIterator(root);
 * while (i.hasNext()) cout << i.next();
 */
