#include<bits/stdc++.h>
using namespace std;
bool detectLoop(Node* head)
{
    unordered_set<Node*> s; 
    while (head != NULL) { 
        if (s.find(head) != s.end()) 
            return true; 
        s.insert(head); 
        head = head->next; 
    } 
    return false;
}
