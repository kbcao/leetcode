class Solution {
    final int N = -666, Y = -233;
    public int firstMissingPositive(int[] nums) {
        for (int i = 0; i < nums.length; ++i) {
            if (nums[i] <= 0 || nums[i] > nums.length) nums[i] = N;
            else if (nums[i] == i + 1) nums[i] = Y;
        }
        for (int i = 0; i < nums.length;) {
            if (nums[i] == Y || nums[i] == N) ++i;
            else if (nums[nums[i] - 1] == Y) nums[i] = N;
            else {
                int v = nums[nums[i] - 1];
                nums[nums[i] - 1] = Y;
                nums[i] = v == i + 1 ? Y : v;
            }
        }
        for (int i = 0; i < nums.length; ++i) {
            if (nums[i] == N) return i + 1;
        }
        return nums.length + 1;
    }
}