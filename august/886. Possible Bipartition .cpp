class Solution {
public:
    bool possibleBipartition(int n, vector<vector<int>>& dislikes) {
        vector<int> color(n+1, -1);
        vector<vector<int>> graph(n+1);
        for (int i = 0; i < dislikes.size(); ++i) {
            graph[dislikes[i][0]].push_back(dislikes[i][1]);
            graph[dislikes[i][1]].push_back(dislikes[i][0]);
        }
        for (int i = 1; i <= n; ++i) {
            if (color[i] == -1) {
                queue<int> q;
                q.push(i);
                color[i] = 0;
                while (!q.empty()) {
                    int node = q.front();
                    q.pop();
                    for (int j = 0; j < graph[node].size(); ++j) {
                        if (color[graph[node][j]] == -1) {
                            color[graph[node][j]] = 1 - color[node];
                            q.push(graph[node][j]);
                        } else if (color[graph[node][j]] == color[node]) {
                            return false;
                        }
                    }
                }
            }
        }
        return true;
    }
};