#include <bits/stdc++.h> 
using namespace std; 
//find the node which points to already visited and make it's next as NULL
void removeLoop(Node* head)
{
    unordered_map<Node*, int> node_map; 
    Node* last = NULL;
    while (head != NULL) { 
        if (node_map.find(head) == node_map.end()) { 
            node_map[head]++; 
            last = head; 
            head = head->next; 
        }
        else { 
            last->next = NULL; 
            break; 
        } 
    } 
}