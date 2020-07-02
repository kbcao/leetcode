vector<vector<int>> *matp;
struct cmp {
    bool operator()(pair<int, int>& a, pair<int, int>& b){
        if ((*matp)[a.first][a.second] == (*matp)[b.first][b.second]) {
            if (a.first == b.first) return a.second > b.second;
            return a.first > b.first;
        }
        return (*matp)[a.first][a.second] > (*matp)[b.first][b.second];
    }
};

class Solution {
public:
    int kthSmallest(vector<vector<int>>& mat, int k) {
        matp = &mat;
        priority_queue<pair<int, int>, vector<pair<int, int>>, cmp> pq;
        pq.push(make_pair(0, 0));
        int last_x = -1, last_y = -1;
        pair<int, int> node;
        while (k) {
            node = pq.top();
            pq.pop();
            int x = node.first, y = node.second;
            if (x == last_x && y == last_y) continue;
            last_x = x, last_y = y;
            --k;
            if (x + 1 < mat.size()) {
                pq.push(make_pair(x + 1, y));
            }
            if (y + 1 < mat[0].size()) {
                pq.push(make_pair(x, y + 1));
            }
        }
        return mat[node.first][node.second];
    }
};