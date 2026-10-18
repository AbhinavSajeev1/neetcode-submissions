class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sequence = set(nums)
        longest = 0
        for num in sequence:
            if (num-1) not in sequence:
                length = 1
                while (num + length) in sequence:
                    length += 1
                longest = max(longest, length)
        return longest

            