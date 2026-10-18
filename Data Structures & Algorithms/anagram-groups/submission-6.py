class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for string in strs:
            count = [0] * 26
            for s in string: 
                val = ord(s) - ord("a")
                count[val] +=1 
            hashmap[tuple(count)].append(string)
        return list(hashmap.values())
