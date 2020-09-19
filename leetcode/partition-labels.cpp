class Solution {
public:
    vector<int> partitionLabels(string S) {
        int i = 0, k = 0, start = 0;
        vector<int> ret;
        unordered_map<char, int> M;             //stores rightmost occurance of a character
        for(i = 0; i< S.size();i++)
        {
            if (M.find(S[i]) == M.end())
                M.insert(make_pair(S[i], i));
            else
                M[S[i]] = max(M[S[i]], i);   
        }
        // for(auto j : M)
        // {
        //     cout<<j.first<<" "<<j.second<<endl;
        // }        
        for(i = 0;i < S.size();i++)
        {
            k = max(k, M[S[i]]);
            if(i==k)
            {
                ret.push_back(i-start+1);
                start = i + 1;
            }
        }
        return ret;
    }
};