#include<bits/stdc++.h>
using namespace std;
#define ll long long

vector<ll>vec;
stack <pair<ll,ll>>s;   // {element, index}
ll ans[1000006],n;

void nextmax()
{
    s.push({vec[0],0});     // Push first element
    int i;
    
    i=1;    // Start comparing from second element
    while(i<n)
    {
        while(i<n && !s.empty() && vec[i]>s.top().first)
        {
            ans[s.top().second]=vec[i]; // Storing ans[index]=next_greater_element
            s.pop();
        }
        
        s.push({vec[i],i});
        i++;
    }
}

int main()
{
    ll i,j,t,x;
    cin>>t;
    
    while(t--)
    {
        while(!s.empty())
            s.pop();
        vec.clear();
        memset(ans,-1,sizeof(ans)); // By default, no element has a next_greater_element
        
        cin>>n;
        for(i=0; i<n; i++){
            cin>>x;
            vec.push_back(x);
        }
            
        nextmax();
            
        for(i=0; i<n; i++)
            cout<<ans[i]<<" ";
        cout<<endl;
    }
}