class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for string in strs:
            key = ''.join(sorted(string))
            anagrams.setdefault(key, [])
            anagrams[key].append(string)
        output = []
        for anagram_list in anagrams.values():
            output.append(anagram_list)
            
        return output

            
        