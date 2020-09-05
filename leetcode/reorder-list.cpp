class Solution {
public:
    void merge(ListNode *first, ListNode **second)  
    {  
        ListNode *p_curr = first, *second_curr = *second;  
        ListNode *first_next, *second_next;
        while (first_curr != NULL && second_curr != NULL)  
        {  
            first_next = first_curr->next;  
            second_next = second_curr->next;
            second_curr->next = first_next;
            first_curr->next = second_curr;
            first_curr = first_next;  
            second_curr = second_next;  
        }  
        *second = second_curr;
    }
    void reorderList(ListNode* head)
    {
        ListNode* temp = head;
        if (head==NULL) return;
        int length = 0;
        while(temp)
        {
            temp = temp->next;
            length++;
        }
        ListNode* slow = head;
        ListNode* fast = head;
        ListNode* prev = NULL;
        while(fast!=NULL && fast->next!=NULL)               //reaches middle element
        {
            prev = slow;
            slow = slow->next;
            fast = fast->next->next;
        }
        if(length%2==1)
        {
            temp = slow->next;
            slow->next = NULL;
        }
        else
        {
            temp = slow;
            prev->next = NULL;
        } 
        prev = NULL;
        ListNode* nextt;
        while(temp)                                       //reverses second half
        {
            nextt = temp->next;
            temp->next = prev;
            prev = temp;
            temp = nextt;
        }
        temp = prev;
        merge(head, &temp);                               //alternatively merges elements
    }
};