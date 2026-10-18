class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for string in strs:
            count = [0] * 26
            for s in string:
                val = ord(s) - ord("a")
                count[val] += 1
            res[tuple(count)].append(string)
        return list(res.values())             