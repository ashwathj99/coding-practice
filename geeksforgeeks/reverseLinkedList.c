// Should reverse list and return new head.
struct Node* reverseList(struct Node *head)
{
    // code here
    Node* prev = NULL;
    Node* curr = head;
    Node* next = NULL;
    while(curr!=NULL)
    {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }
    head = prev;
    return head;
    // return head of reversed list
}