class Solution {
public:
    double new21Game(int N, int K, int W) {
        if (K == 0) return 1;
        double arr[10007];
        memset(arr, 0, sizeof(arr));
        arr[0] = 1;
        for (int i = 1; i <= N; ++i) {
            arr[i] = (arr[min(i, K) - 1] - (i - 1 - W < 0 ? 0.0 : arr[i - 1 - W])) / W + arr[i - 1];
        }
        return arr[N] - arr[K - 1];
    }
};