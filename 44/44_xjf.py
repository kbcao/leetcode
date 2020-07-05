class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if p == '': return s == ''
        vis = [[False for j in range(len(p) + 1)] for i in range(len(s) + 1)]
        def dfs(si, pi):
            if vis[si][pi]: return False
            vis[si][pi] = True
            if pi == len(p): return si == len(s)
            if si == len(s): return (dfs(si, pi + 1) if p[pi] == '*' else False)
            if p[pi].isalpha() and s[si] != p[pi]: return False
            if p[pi] != '*': return dfs(si + 1, pi + 1)
            else:
                for ssi in range(si, len(s) + 1):
                    if dfs(ssi, pi + 1): return True
            return False
        return dfs(0, 0)
