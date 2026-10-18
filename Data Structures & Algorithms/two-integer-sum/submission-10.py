class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}


        for i, v in enumerate(nums):
            difference = target - v 
            if difference in hashmap:
                return [hashmap[difference], i]
            hashmap[v] = i 

