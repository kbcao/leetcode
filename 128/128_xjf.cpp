class Solution {
public:
    unordered_map<int, int> mp;
    int longestConsecutive(vector<int>& nums) {
        if (nums.size() == 0) return 0;
        for (auto &n : nums) mp[n] = 0;
        int res = 1;
        for (auto &p : mp) res = max(check(p.first), res);
        return res;
    }

    int check(int n) {
        if (mp[n] > 0) return mp[n];
        if (mp.find(n - 1) != mp.end())
            return mp[n] = check(n - 1) + 1;
        return mp[n] = 1;
    }
};