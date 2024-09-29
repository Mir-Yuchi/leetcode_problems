//
// Created by kimiho on 9/29/24.
//

class Solution {
public:
    int scoreOfString(string s) {
        int sum = 0;
        for( int i=0; i<s.size()-1; ++i){
            sum += abs(s[i]-s[i+1]);
        }
        return sum;
    }
};