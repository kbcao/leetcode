class Solution {
public:
    char parent['z' + 7];
    char find(char c) { return parent[c] - c ? parent[c] = find(parent[c]) : c; }
    char unite(char c1, char c2) { return parent[find(c1)] = find(c2); }
    bool equationsPossible(vector<string>& equations) {
        for (char i = 'a'; i <= 'z'; ++i) parent[i] = i;
        for(auto &s : equations)
            if (s[1] == '=') unite(s[0], s[3]);
        for(auto &s : equations)
            if (s[1] == '!' && find(s[0]) == find(s[3])) return false;
        return true;
    }
};