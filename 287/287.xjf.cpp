class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        int res = 0;
        int bit = 1;
        while (bit > 0) {
            int cnt = 0;
            for (int &num : nums) if (num & bit) ++cnt;
            for (int i = 1; i < nums.size(); ++i) if (i & bit) --cnt;
            if (cnt > 0) res |= bit;
            bit <<= 1;
        }
        return res;
    }
};