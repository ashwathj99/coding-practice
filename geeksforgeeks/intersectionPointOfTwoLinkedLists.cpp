#include <bits/stdc++.h> 
using namespace std; 
int intersectPoint(Node* head1, Node* head2)
{
    set<Node*> s;
	Node* temp1=head1,*temp2=head2;
	while(temp1){
		s.insert(temp1);
		temp1=temp1->next;
	}
	while(temp2){
		if(s.find(temp2)==s.end()){
			temp2=temp2->next;
		}
		else{
			return temp2->data;
		}
	}
	return -1;
}