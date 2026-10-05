class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        largest = -1
        for i in reversed(range(len(arr))):
            nextlargest = max(largest, arr[i])
            arr[i] = largest
            largest = nextlargest


        return arr

            
