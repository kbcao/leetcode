//这题和第十题正则表达式一样, 比第十题还简单一点
class Solution {
    boolean vis[][];
    public boolean isMatch(String s, String p) {
        vis = new boolean[s.length() + 3][p.length() + 3];
        return isMatch(s, p, 0, 0);
    }

    private boolean isMatch(String s, String p, int si, int pi) {
        if (vis[si][pi]) return false;
        for (;pi < p.length(); ++pi) {
            if (p.charAt(pi) == '?' || (si < s.length() && p.charAt(pi) == s.charAt(si))) ++si;
            else if (p.charAt(pi) == '*') {
                while (si < s.length()) {
                    if (isMatch(s, p, si, pi + 1)) return true;
                    vis[si++][pi + 1] = true;
                }
            }
            else return false;
        }
        return si == s.length();
    }
}