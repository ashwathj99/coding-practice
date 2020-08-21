Node *removeDuplicates(Node *root)
{
    int curr=root->data;
    Node* res = root;
    Node* prev = root;
    root = root->next;
    Node* temp;
    while(root)
    {
        if(curr==root->data)
        {
            temp = root;
            prev->next = root->next;
            root = root->next;
            free(temp);
        }
        else
        {
            curr = root->data;
            prev = root;
            root = root->next;
        }
    }
    return res;
}