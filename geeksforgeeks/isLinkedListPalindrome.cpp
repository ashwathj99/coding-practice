// reverse second half and check with each node of first half

void reverse(struct Node** head)
{
    struct Node* prev = NULL;
    struct Node* curr = *head;
    struct Node* next;
    while(curr!=NULL)
    {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }
    *head = prev;
}
bool compareLists(struct Node* head1, struct Node* head2)
{
    struct Node* temp1 = head1;
    struct Node* temp2 = head2;
    while(temp1 && temp2)
    {
        if(temp1->data==temp2->data)
        {
            temp1 = temp1->next;
            temp2 = temp2->next;
        }
        else    return 0;
    }
    if(temp1==NULL && temp2==NULL)  return 1;
    return 0;
}
bool isPalindrome(Node *head)
{
    Node *slow = head, *fast = head;
    Node *second_half, *prevofslow = head;
    Node* mid = NULL;
    bool res = true;
    if(head!=NULL && head->next!=NULL)
    {
        while(fast!=NULL && fast->next!=NULL)
        {
            prevofslow = slow;
            slow = slow->next;
            fast = fast->next->next;
        }
        if(fast!=NULL)
        {
            mid = slow;
            slow = slow->next;
        }
        second_half = slow;
        prevofslow->next = NULL;
        reverse(&second_half);
        res = compareLists(head, second_half);
        reverse(&second_half);
        if(mid!=NULL)
        {
            prevofslow->next = mid;
            mid->next = second_half;
        }
        else    prevofslow->next = second_half;
    }
    return res;
}
//smaller
// Node* reverse(Node* slow)
//    {
//        Node* curr=slow;
//        Node* next;
//        Node* prev=NULL;
//        while(curr!=NULL)
//        {
//            next=curr->next;
//            curr->next=prev;
//            prev=curr;
//            curr=next;
           
//        }
//        return prev;
//    }
// bool isPalindrome(Node *head)
// {
//     Node* slow=head;
//           Node*  fast=head;
//         while(fast!=NULL && fast->next!=NULL)
//         {
//            slow=slow->next;
//             fast=fast->next->next;
//         } 
//         fast=head;
//         slow=reverse(slow);
//         // return checkit(str);
//         while(slow!=NULL)
//         {
//             if(fast->data!=slow->data)
//             {
//                 return false;
//             }  
//             slow=slow->next;
//             fast=fast->next;
//         } 
//         return true;
// }

//much smaller absolute madlad hacks \\only for single digit numbers
// bool isPalindrome(Node *head)
// {
//     struct Node *p;
//     p=head;
//     int t1=0,t2=0,n=1;
//     while(p!=NULL)
//     {
//         t1=t1+(p->data*n);
//         t2=(t2*10)+p->data;
//         p=p->next;
//         n=n*10;
//     }
//     if(t1==t2)
//         return 1;
//     else
//         return 0;
// }