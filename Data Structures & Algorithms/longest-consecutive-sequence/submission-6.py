class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        largest = 0
        for num in num_set:
            if num - 1 not in num_set:
                count = 1
                curr = num
                while(True):
                    if curr + 1 in num_set:
                        count+=1;
                        curr = curr + 1
                    else:
                        largest = max(count, largest)
                        break


        return largest