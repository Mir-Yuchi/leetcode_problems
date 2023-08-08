class Solution {
public:
    int divide(int dividend, int divisor) {
        if(dividend == INT_MIN && divisor == -1) {
            return INT_MAX;
        }
        long long int a = abs(dividend), b = abs(divisor), res = 0;
        int sign = (dividend < 0) ^ (divisor < 0) ? -1 : 1;
        while(a >= b) {
            long long int temp = b, count = 1;
            while(temp << 1 <= a) {
                temp <<= 1;
                count <<= 1;
            }
            a -= temp;
            res += count;
        }
        return sign * res;
    }
};