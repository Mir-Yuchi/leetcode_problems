class Solution {
public:
    int minNumber(vector<int> &nums1, vector<int> &nums2) {
        sort(nums1.begin(), nums1.end());
        sort(nums2.begin(), nums2.end());

        for (int i: nums1) {
            for (int j: nums2) {
                if (i == j) {
                    return i;
                }
            }
        }
        int min1 = *min_element(nums1.begin(), nums1.end());
        int min2 = *min_element(nums2.begin(), nums2.end());

        if (min1 < min2) return min1 * 10 + min2;

        return min2 * 10 + min1;
    }
};