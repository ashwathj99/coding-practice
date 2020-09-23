class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        if(n<2) return 0;
        int  i, m = height[0];
        vector<int> left, right;
        left.push_back(height[0]);
        for(i=1;i<n;i++)
            left.push_back(max(left[i-1],height[i]));
        right.push_back(height[n-1]);
        for(i=1;i<n-1;i++)
            right.push_back(max(right[i-1],height[n-1-i]));
        right.push_back(height[0]);
        int total = 0;
        for(i=0;i<n;i++)
            total=total+min(left[i],right[n-1-i]) - height[i];
        return total;
    }
}