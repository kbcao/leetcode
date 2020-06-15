class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 0) return "";
        for (int i = 0; i < strs[0].length(); ++i) for (String s : strs) {
            try { if (s.charAt(i) == strs[0].charAt(i)) continue; }
            catch (Exception ignored) {}
            return strs[0].substring(0, i);
        }
        return strs[0];
    }
}