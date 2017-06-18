/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
int Solution::t2Sum(TreeNode* A, int B) {
    stack <TreeNode*> st1;
    stack <TreeNode*> st2;
    TreeNode *curr1 = A, *curr2 = A;
    int done1 = 0, done2 = 0, val1, val2;
    while(1){
        while( done1 == 0){
            if( curr1!=NULL){
                st1.push(curr1);
                curr1 = curr1 -> left;
            }
            else{
                if( st1.empty())
                    done1 = 1;
                else
                {
                    curr1 = st1.top();st1.pop();
                    val1 = curr1->val;
                    curr1 = curr1->right;
                    done1 = 1;
                }
            }
        }
        while (done2 == 0)
        {
            if (curr2 != NULL){
                st2.push(curr2);
                curr2 = curr2->right;
            }
            else{
                if (st2.empty())
                    done2 = 1;
                else{
                    curr2 = st2.top();st2.pop();
                    val2 = curr2->val;
                    curr2 = curr2->left;
                    done2 = 1;
                }
            }
        }

        if ((val1 != val2) && (val1 + val2) == B)
            return 1;
        else if ((val1 + val2) < B)
            done1 = 0;
        else
            done2 = 0;

        if (val1 >= val2)
            return 0;
    }
    return 0;
}

