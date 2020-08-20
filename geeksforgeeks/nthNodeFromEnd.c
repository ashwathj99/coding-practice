int getNthFromLast(Node *head, int n)
{
       // Your code here
        int i = 1;
        Node* temp = head;
        while(temp!=NULL)
        {
            temp = temp->next;
            i+=1;
        }
        i-=1;
        temp = head;
        if(n>i)  return -1;
        while(i-n>0)
        {
            temp=temp->next;
            n++;
        }
        return temp->data;
}