class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        int mx= -1;
        for (auto e : candies) mx = max(e, mx);
        vector<bool> res(candies.size());
        for (int i = 0; i < candies.size(); ++i) res[i] = candies[i] + extraCandies >= mx;
        return res;
    }
};