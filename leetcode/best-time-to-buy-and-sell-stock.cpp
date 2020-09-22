class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if (prices.size()==0) return 0;
        int m = 1000000, i;
        vector<int> mins, maxs;
        for(i = 0; i<prices.size();i++)         //min price till ith day
        {
            m = min(m, prices[i]);
            mins.push_back(m);
        } m = -1;
        reverse(prices.begin(), prices.end());
        for(i = 0; i < prices.size();i++)
        {
            m = max(m,prices[i]);
            maxs.push_back(m);
        } m = -1;
        reverse(maxs.begin(), maxs.end());   //max price you can get bryond ith day
        for(i = 0;i<maxs.size();i++)
        {
            m = max(maxs[i]-mins[i], m);
        }
        return m;
    }
};