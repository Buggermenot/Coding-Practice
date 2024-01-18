class Solution {
public:
    unordered_map<int , int> indices;

    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            indices[nums[i]] = i+1;
        }

        int a, b;
        vector<int> res(2);
        for (int i = 0; i < n; i++) {
            int b = target - nums[i];
            if (indices[b] && indices[b] != i+1) {
                return {i, indices[b] - 1};
            }
        }

        return {};
    }
};