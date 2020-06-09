class Solution {
    public int translateNum(int num) {
        int res = 1, last = 1;
        while (num > 0) {
            int _last = res;
            int t = num % 100;
            if (t >= 10 && t <= 25) res += last;
            num /= 10;
            last = _last;
        }
        return res;
    }
}