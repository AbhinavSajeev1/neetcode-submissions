class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, j in enumerate(nums):
            difference = target - j 
            if difference in hashmap:
                return list((hashmap[difference], i))
            hashmap[j] = i
