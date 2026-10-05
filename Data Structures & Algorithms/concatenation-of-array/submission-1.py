class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        arr = []

        for i in range(2):
            for n in nums:
                arr.append(n)
        
        return arr

        

