class Solution {
    typedef long long ll;
public:
    int splitArray(vector<int>& nums, int m) {
        ll left = 0, right = 1;
        for (const auto& v : nums) {
            left = max(left, (ll)v);
            right += v;
        }
        while (left < right) {
            ll mid = left + right >> 1;
            int mm = m;
            ll cur = 0;
            for (const auto& v : nums) {
                if (cur + v > mid) {
                    cur = v;
                    --mm;
                }
                else cur += v;
            }
            if (mm < 1) left = mid + 1;
            else right = mid;
        }
        return left;
    }
};