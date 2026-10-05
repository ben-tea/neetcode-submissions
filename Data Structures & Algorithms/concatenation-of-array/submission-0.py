class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        arr = [0] * length * 2

        for i in range(length):
            arr[i] = nums[i]
            arr[length + i] = nums[i]
        
        return arr

        

