int dp[501][501];
int maxAlice(int start, int end, vector<int>& v)
{
    if(start > end) return 0;
    if(dp[start][end]!=-1) return dp[start][end];
    int left = 0, right = 0, answer = 0;
    for(int i = start; i <= end ; i++)
        right+=v[i];
    for(int i = start ; i < end ; i++)
    {
        left+=v[i];
        right-=v[i];
        if(left < right)
            answer = max(answer, left + maxAlice(start, i, v));
        if(left == right)
            answer = max(answer, left + max(maxAlice(start, i, v), maxAlice(i+1, end, v)));
        if(right < left)
            answer = max(answer, right + maxAlice(i+1, end, v));
    }
    return dp[start][end] = answer;
}
int stoneGameV(vector<int>& v)
{
    memset(dp, -1, sizeof dp);
    return maxAlice(0, v.size() - 1, v);
}