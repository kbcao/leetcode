class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        // 法1: 二分
        // int l = 1, r = nums.size();
        // while (l + 1 < r) {
        //     int m = l + r >> 1;
        //     int cnt = 0;
        //     for (int &num : nums) cnt += num < m;
        //     if (cnt < m) l = m;
        //     else r = m;
        // }
        // return l;

        // 法2: 按位
        // int res = 0;
        // int bit = 1;
        // while (bit > 0) {
        //     int cnt = 0;
        //     for (int &num : nums) if (num & bit) ++cnt;
        //     for (int i = 1; i < nums.size(); ++i) if (i & bit) --cnt;
        //     if (cnt > 0) res |= bit;
        //     bit <<= 1;
        // }
        // return res;

        // 法3: 快慢指针
        if (nums[0] == nums[nums.size() - 1]) return nums[0];
        int fast = 0, slow = 0;
        do {
            fast = nums[nums[fast]];
            slow = nums[slow];
        } while (fast != slow);
        slow = 0;
        while (fast != slow) {
            fast = nums[fast];
            slow = nums[slow];
        }
        return slow;
    }
};