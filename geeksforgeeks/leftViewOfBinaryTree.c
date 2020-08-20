//first element of each level order traversal
void func(struct Node* root, int level, int* max_level)
{
    if (root==NULL) return;
    if (*max_level<level)
    {
        printf("%d ", root->data);
        *max_level = level;
    }
    func(root->left, level+1, max_level);
    func(root->right, level+1, max_level);  
}
void leftView(Node *root)
{
   // Your code here
   int max_level = 0;
   func(root,1,&max_level);
}