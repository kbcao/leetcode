class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> res(nums.size());
        res[0] = 1;
        for (int i = 1; i < res.size(); ++i) res[i] = nums[i - 1] * res[i - 1];
        int pro = 1;
        for (int i = res.size() - 1; i >=0; --i) {
            res[i] *= pro;
            pro *= nums[i];
        }
        return res;
    }
};