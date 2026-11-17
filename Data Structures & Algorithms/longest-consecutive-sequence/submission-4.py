class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        last = nums[0]
        print(nums)
        count = 1
        longest = 1
        for num in nums:
            if num == last:
                continue
            if num - 1 == last:
                count += 1
            else:
                longest = max(count, longest)
                count = 1


            last = num

        longest = max(count, longest)

        return longest


