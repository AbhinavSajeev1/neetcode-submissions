class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} 
        for i, v in enumerate(nums):
            result = target - v
            if result in hashmap:
                return [hashmap[result], i]
            hashmap[v] = i
