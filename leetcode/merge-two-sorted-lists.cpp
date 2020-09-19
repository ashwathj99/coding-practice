/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if(l1==NULL)    return l2;
        if(l2==NULL)    return l1;
        if(l1->val > l2->val)
        {
            ListNode* temp = l1;
            l1 = l2;
            l2 = temp;
        }
        ListNode* t1 = l1->next, *t2 = l2, *prev = l1;
        while(t1 && t2)
        {
            if(t1->val <= t2->val)
            {
                prev->next = t1;
                prev = t1;
                t1 = t1->next;
            }
            else
            {
                prev->next = t2;
                prev = t2;
                t2 = t2->next;
            }
        }
        if(t1)      prev->next = t1;
        if(t2)      prev->next = t2;
        
        return l1;
    }
};