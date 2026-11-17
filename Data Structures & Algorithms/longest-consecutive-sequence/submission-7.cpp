class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        std::unordered_set<int> numSet(nums.begin(), nums.end());

        int largest = 0;

        for(int num : numSet){
            if(!numSet.contains(num - 1)){
                int count = 1;
                int curr = num;
                while(true){
                    if(numSet.contains(curr + 1)){
                        count++;
                        curr++;
                    }else{
                        largest = std::max(count, largest);
                        break;
                    }
                }
            }
        }
        return largest;
    }
};
