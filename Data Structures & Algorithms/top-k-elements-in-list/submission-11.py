class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]: 

        buckets = []
        bucket = []
        nums = sorted(nums)
        for i in range(len(nums) - 1):
            bucket.append(nums[i])
            if nums[i] != nums[i + 1]:
                buckets.append(bucket)
                bucket = []
        # edge case: we need to append the last value after the loop ends
        bucket.append(nums[-1])
        buckets.append(bucket)
            


        output = []
        buckets = sorted(buckets, key=lambda x: len(x), reverse=True)

        for i in range(k):
            output.append(buckets[i][0])
            
        return output

            
            


        