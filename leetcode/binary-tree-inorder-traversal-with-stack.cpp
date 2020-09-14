class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int>nodes;
        stack<TreeNode*> stk;
        while ( root || !stk.empty())
        {
            while(root)
            {
                stk.push(root);
                root = root->left;
            }
            root = stk.top(); 
            stk.pop();
            nodes.push_back(root->val);
            root = root->right;
        }
        return nodes;
    }
};