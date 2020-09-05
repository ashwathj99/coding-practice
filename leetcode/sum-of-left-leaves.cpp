class Solution {
public:
    int sum = 0;
    void func(TreeNode* root, int n)
        {
            if(root==NULL)
                return;
            func(root->left, 1);
            if(root->left==NULL && root->right == NULL && n == 1)
            {
                sum+=root->val;
            }
            func(root->right, 2);
        }
    int sumOfLeftLeaves(TreeNode* root) {
        func(root, 0);
        return sum;
    }
};