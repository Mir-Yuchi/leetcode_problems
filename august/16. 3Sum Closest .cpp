class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        int n = nums.size(), l, r, sum, ans = nums[0] + nums[1] + nums[2];
        sort(nums.begin(), nums.end());
        for (int i = 0; i < n - 2; ++i) {
            l = i + 1, r = n - 1;
            while (l < r) {
                sum = nums[i] + nums[l] + nums[r];
                if (abs(target - sum) < abs(target - ans)) ans = sum;
                if (sum < target) ++l;
                else --r;
            }
        }
        return ans;
    }
};