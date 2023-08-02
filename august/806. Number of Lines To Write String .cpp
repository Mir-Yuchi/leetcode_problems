#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    vector<int> numberOfLines(vector<int>& widths, string s) {
        int lines = 1, width = 0;
        for (int i = 0; i < s.size(); ++i) {
            width += widths[s[i]-'a'];
            if(width > 100) {
                lines++;
                width = widths[s[i]-'a'];
            }
        }
        return {lines, width};
    }
};