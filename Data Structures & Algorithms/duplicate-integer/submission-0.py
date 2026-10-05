class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_dict = {}
        for i in range(len(nums)):
            my_dict[nums[i]] = i
        
        for i in range(len(nums)):
            if nums[i] in my_dict and my_dict.get(nums[i]) != i:
                return True

        return False
            