#include "bits/stdc++.h"

using namespace std;

vector<vector<int>> combine(int n, int k) {
    vector<vector<int>> ans;
    vector<int> temp;
    function<void(int)> dfs = [&](int idx) {
        if (temp.size() == k) {
            ans.push_back(temp);
            return;
        }
        for (int i = idx; i <= n; i++) {
            temp.push_back(i);
            dfs(i + 1);
            temp.pop_back();
        }
    };
    dfs(1);
    return ans;
}