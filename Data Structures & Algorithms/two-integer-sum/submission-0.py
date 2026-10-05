class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}

        for i in range(len(nums)):
            my_dict[nums[i]] = i

        for i in range(len(nums)):
            pair = target - nums[i]
            if pair in my_dict and my_dict.get(pair) != i:
                return [i, my_dict.get(pair)]
        
        return []
            

        

