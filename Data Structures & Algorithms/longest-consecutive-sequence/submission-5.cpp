class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if(nums.size() == 0){
            return 0;
        }

        std::sort(nums.begin(), nums.end());
        int pre = nums[0];
        int count = 1;
        int largest = 1;
        for(int num: nums){
            if(pre == num){
                continue;
            }else if(pre == num - 1){
                count++;
            }else{
                largest = std::max(count, largest);
                count = 1;
            }
            pre = num;
        }

        largest = std::max(count, largest);
        return largest;
    }
};
