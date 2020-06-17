class Solution {
    public int maxScoreSightseeingPair(int[] A) {
        int maxj = 0x80000000, res = 0;
        for (int i = A.length - 2; i >= 0; --i) {
            maxj = Math.max(maxj, A[i + 1] - i - 1);
            res = Math.max(res, maxj + A[i] + i);
        }
        return res;
    }
}