# DFS 找连通分量
class Solution:
    var_t, var_f, tags = None, None, None
    def equationsPossible(self, equations: List[str]) -> bool:
        self.var_t, self.var_f, self.tags = {}, {}, {}
        for eq in equations:
            var1, sign, var2 = eq[0], eq[1] == '=', eq[3]
            if var1 not in self.var_t: self.var_t[var1] = []
            if var2 not in self.var_t: self.var_t[var2] = []
            if var1 not in self.var_f: self.var_f[var1] = []
            if var2 not in self.var_f: self.var_f[var2] = []
            if sign:
                self.var_t[var1].append(var2)
                self.var_t[var2].append(var1)
            else:
                self.var_f[var1].append(var2)
                self.var_f[var2].append(var1)
        
        for var1 in self.var_t: self.dfs(var1, var1)
        
        for var1 in self.var_f:
            for var2 in self.var_f[var1]:
                if self.tags[var1] == self.tags[var2]: return False
        return True
    
    def dfs(self, var1, tag):
        if var1 in self.tags: return
        self.tags[var1] = tag
        for var2 in self.var_t[var1]: self.dfs(var2, tag)