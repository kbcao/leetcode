/*
使不使用 vis 数组的差距:
       Time     Memory
使用   12 ms    8 MB
不用   824 ms   90.7 MB
用了 vis 不仅速度快了, 内存占用还少了.

本来时间和内存都击败了百分之个位数的用户, 用了 vis 之后:
执行用时: 12 ms, 在所有 C++ 提交中击败了 70.12% 的用户
内存消耗: 8 MB, 在所有 C++ 提交中击败了 100.00% 的用户
*/

class Solution {
public:
    bool **vis;
    bool isMatch(string s, string p, int pi = 0, int si = 0) {
        if (!p.size()) return !s.size();
        if (!pi) {
            vis = new bool*[p.size() + 3];
            for (int i = 0; i < p.size() + 3; ++i) {
                vis[i] = new bool[s.size() + 3];
                memset(vis[i], 0, sizeof(bool)*(s.size() + 3));
            }
        }
        if (vis[pi][si]) return false;
        for (; pi < p.size(); ++pi) {
            if (p[pi] == '*') continue;
            bool star = pi + 1 < p.size() && p[pi + 1] == '*';
            bool dot = p[pi] == '.';
            if (star) {
                while (si < s.size() && (dot || p[pi] == s[si])) {
                    if (isMatch(s, p, pi + 2, si)) return true;
                    vis[pi][si++] = true;
                }
            }
            else if (si < s.size() && (dot || p[pi] == s[si])) ++si;
            else return false;
        }
        return si == s.size();
    }
};