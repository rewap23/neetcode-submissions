class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> seen; //initializing an unordered set named seen to keep track of values in nums that we have seen
        for (int num: nums) {
            if (seen.count(num)) {
                return true;
            }
            seen.insert(num);
        }
        return false;
    }
};