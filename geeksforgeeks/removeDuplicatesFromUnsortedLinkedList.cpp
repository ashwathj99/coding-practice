#include <bits/stdc++.h> 
using namespace std; 
Node * removeDuplicates( Node *head) 
{
    Node* prev = NULL;
	Node* curr = head;
	unordered_set<int> set;
	while (curr != NULL)
	{
		if (set.find(curr->data) != set.end())
			prev->next = curr->next;
		else
		{
			set.insert(curr->data);
			prev = curr;
		}
		curr = prev->next;
	}
	return head;
}