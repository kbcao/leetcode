class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int res = 0x7f7f7f7f;
        for (int i = 0; i < nums.size() - 2; ++i) {
            int l = i + 1, r = nums.size() - 1;
            while (l < r) {
                int v = nums[i] + nums[l] + nums[r];
                if (abs(v - target) < abs(res - target)) res = v;
                if (v < target) ++l;
                else if (v > target) --r;
                else return target;
            }
        }
        return res;
    }
};