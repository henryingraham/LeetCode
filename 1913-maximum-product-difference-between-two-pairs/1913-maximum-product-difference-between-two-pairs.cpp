class Solution {
public:
    int maxProductDifference(vector<int>& nums) {
        int w = nums[0];
        int x = 0;
        int y = nums[0];
        int z = 10000;
        for(int i = 1; i < nums.size(); i++){
            if(nums[i] > w){
                x = w;
                w = nums[i];
            }
            else if(nums[i] > x){
                x = nums[i];
            }
            if(nums[i] < y){
                z = y;
                y = nums[i];
            }
            else if(nums[i] < z){
                z = nums[i];
            }
                
            
        }
        return (w*x) - (y*z);
    }
};