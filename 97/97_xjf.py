class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3): return False
        vis = [[False for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        def dfs(i1, i2):
            if i1 == len(s1) and i2 == len(s2): return True
            if vis[i1][i2]: return False
            vis[i1][i2] = True
            i3 = i1 + i2
            if i1 < len(s1) and s1[i1] == s3[i3]:
                if dfs(i1 + 1, i2): return True
            if i2 < len(s2) and s2[i2] == s3[i3]:
                if dfs(i1, i2 + 1): return True
            return False
        return dfs(0, 0)