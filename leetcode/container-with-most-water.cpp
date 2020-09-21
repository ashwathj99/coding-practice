class Solution {
public:
    int maxArea(vector<int>& height) {
        int areaMax = 0, l = 0, r  = height.size()-1;
        while(l < r)
        {
            areaMax = max(areaMax, min(height[l], height[r]) * (r-l));
            // cout<<l<<" "<<r<<endl;
            if(height[l] < height[r])
                l++;
            else
                r--;
        }
        return areaMax;
    }
};