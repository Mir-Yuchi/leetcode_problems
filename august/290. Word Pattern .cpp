class Solution {
public:
    bool wordPattern(string pattern, string s) {
        unordered_map<char, string> m;
        unordered_map<string, char> m2;
        vector<string> v;
        string temp = "";
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == ' ') { v.push_back(temp); temp = ""; }
            else temp += s[i];
        }
        v.push_back(temp);
        if (pattern.size() != v.size()) return false;
        for (int i = 0; i < pattern.size(); i++) {
            if (m.find(pattern[i]) == m.end()) m[pattern[i]] = v[i];
            else if (m[pattern[i]] != v[i]) return false;
            if (m2.find(v[i]) == m2.end()) m2[v[i]] = pattern[i];
            else if (m2[v[i]] != pattern[i]) return false;
        }
        return true;
    }
};