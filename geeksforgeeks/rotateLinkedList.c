//rotate counter-clockwise with 0<=k<=N
Node* rotate(Node* head, int k)
{
    if(k==0) return head;
    Node* curr = head;
    Node* prev = NULL;
    while(k>0 && curr->next!=NULL)
    {
        prev = curr;
        curr = curr->next;
        k--;
    }
    if(curr->next==NULL && k>0) return head;
    Node* newhead = curr;
    Node* temp = curr;
    while(temp->next!=NULL)
        temp = temp->next;
    prev->next = NULL;
    temp->next = head;
    head = newhead;
    return head;
}