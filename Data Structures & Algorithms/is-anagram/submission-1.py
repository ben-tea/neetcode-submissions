class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq1 = {}
        freq2 = {}

        for char in s:
            if char in freq1:
                freq1[char] += 1
            else:
                freq1[char] = 1

        for char in t:
            if char in freq2:
                freq2[char] += 1
            else:
                freq2[char] = 1

        for freq in freq1:
            if freq not in freq2 or freq1[freq] != freq2[freq]:
                return False

        return True

        

        