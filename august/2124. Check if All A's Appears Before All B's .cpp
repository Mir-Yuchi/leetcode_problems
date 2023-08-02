#include <bits/stdc++.h>

using namespace std;

class Solution {
public:
    bool checkString(string s) {
        bool flag = true;
        for (int i = 0; i < s.size(); ++i)
            if(s[i]=='b' and s[i+1]=='a') flag = false;
        return flag;
    }
};