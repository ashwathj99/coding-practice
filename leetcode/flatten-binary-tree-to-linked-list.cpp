class Solution {
public:
    void flatten(TreeNode* root) {
        if(root==NULL)
            return;
        flatten(root->left);
        flatten(root->right);
        TreeNode* rightTemp = root->right;
        if(root->left!=NULL)
        {
            root->right = root->left;
            root->left = NULL;
            while(root->right!=NULL)
            {
                root = root->right;
            }
            root->right = rightTemp;
        }
    }
};