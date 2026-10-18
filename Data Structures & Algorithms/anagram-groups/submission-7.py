class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for string in strs:
            freq = [0] * 26
            for char in string: 
                freq[ord(char) - ord("a")] += 1
            hashmap[tuple(freq)].append(string)
        
        return list(hashmap.values())
        
