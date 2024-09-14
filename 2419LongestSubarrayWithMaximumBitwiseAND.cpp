class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int m = 0;
        for (int i = 0; i < nums.size(); i++){
            if (nums[i] > m)
                m = nums[i];
        }
        int max_count = 0;
        int count = 0;
        for (int i = 0; i < nums.size(); i++){
            if (nums[i] == m)
                count += 1;
            else
                count = 0;
            if(count > max_count)
                max_count = count;
        }
        return max_count;
    }
};
