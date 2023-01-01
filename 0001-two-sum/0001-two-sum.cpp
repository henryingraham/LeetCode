using namespace std;
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> index;
        for(unsigned int i = 0; i < nums.size()-1; i++){
            for(unsigned int j = i+1; j < nums.size(); j++){
                if(nums[i]+nums[j] == target){
                    index.push_back(i);
                    index.push_back(j);
                    return index;
                }
            }
        }
        return index;
    }
};