//Traverse inorder and check if result is ascending. storing prev and check if it lesser than curr then ok
bool inOrderCheck(struct Node* root, Node *&prev) 
{ 
    if (root) 
    { 
        if (!inOrderCheck(root->left, prev))   return false;
        if (prev != NULL && root->data <= prev->data)   return false; 
   
        prev = root; 
        return inOrderCheck(root->right, prev); 
    }
    return true; 
} 
bool isBST(Node *root) 
{ 
   Node *prev = NULL; 
   return inOrderCheck(root, prev); 
}