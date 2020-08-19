int getMiddle(Node *head)
{
   // Your code here
   struct Node *first = head;  
    struct Node *second = head;
    if (head!=NULL)  
    {  
        while (second != NULL && second->next != NULL)  
        {  
            second = second->next->next;  
            first = first->next;  
        }  
        return first->data;  
    }
}