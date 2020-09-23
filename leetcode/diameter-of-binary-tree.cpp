//Max value of Height(leftSubtree)+Height(rightSubtree) (at any node ) is the diameter
class Solution {
public:
    int recurse(TreeNode* root, int &num)
    {
        if(root==NULL)  return 0;
        int l = recurse(root->left, num);
        int r = recurse(root->right, num);
        num = max(num, l+r);
        return max(l,r) + 1;
    }
    int diameterOfBinaryTree(TreeNode* root) {
        int num = 0;
        int nums = recurse(root, num);
        return num;
    }
};