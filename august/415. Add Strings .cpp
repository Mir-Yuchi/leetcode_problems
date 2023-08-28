class Solution {
public:
    string addStrings(string num1, string num2) {
        string ans = "";
        int i = num1.size() - 1, j = num2.size() - 1, carry = 0;
        while (i >= 0 || j >= 0) {
            int sum = carry;
            if (i >= 0) sum += num1[i--] - '0';
            if (j >= 0) sum += num2[j--] - '0';
            ans += to_string(sum % 10);
            carry = sum / 10;
        }
        if (carry) ans += to_string(carry);
        reverse(ans.begin(), ans.end());
        return ans;
    }
};