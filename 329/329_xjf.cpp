class Solution {
public:
    int n, m;
    vector<vector<int>> mat, vis;
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        n = matrix.size();
        if (n == 0) return 0;
        m = matrix[0].size();
        mat = matrix;
        vis = vector<vector<int>>(n, vector<int>(m, -1));

        int res = 0;
        for (int i = 0; i < n; ++i) for (int j = 0; j < m; ++j) {
            res = max(dfs(i, j, -1), res);
        }
        return res;
    }

    int dfs(int x, int y, int last) {
        if (x < 0 || x >= n || y < 0 || y >= m) return 0;
        int cur = mat[x][y];
        if (last != -1 && last <= cur) return 0;
        if (vis[x][y] != -1) return vis[x][y];
        int max_v = max(max(dfs(x - 1, y, cur), dfs(x + 1, y, cur)),
            max(dfs(x, y - 1, cur), dfs(x, y + 1, cur)));
        return vis[x][y] = max_v + 1;
    }
};