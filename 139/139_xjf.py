class Solution:
    trie, vis, s = None, None, None
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.s = s
        self.trie = {}
        for word in wordDict:
            p = self.trie
            for c in word:
                p.setdefault(c, {})
                p = p[c]
            p['*'] = True
        self.vis = [False] * len(s)
        return self.dfs(0)
    
    def dfs(self, idx: int) -> bool:
        if self.vis[idx]: return False
        p = self.trie
        for i in range(idx, len(self.s)):
            if '*' in p:
                if self.dfs(i): return True
            if self.s[i] in p:
                p = p[self.s[i]]
                continue
            self.vis[i] = True
            return False
        return '*' in p
