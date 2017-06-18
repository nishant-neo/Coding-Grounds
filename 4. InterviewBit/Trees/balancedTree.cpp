int max( int a, int  b){
    return a > b ? a :b;
}
int height(TreeNode* A) {
    if( A == NULL)
        return 0;
    return MAX( height( A -> left ), height( A -> right)) + 1;

}
int Solution::isBalanced(TreeNode* A) {
    if( A == NULL)
        return 1;
    int lh = height( A -> left);
    int rh = height( A -> right);
    if( abs(lh -rh ) <= 1 && isBalanced( A -> left) && isBalanced( A -> right) )
        return 1;
    return 0;
}
