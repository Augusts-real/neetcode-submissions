class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0

        for i in nums:
            if (i-1) not in nums:
                length = 0
                while (i + length) in nums:
                    length += 1
                    longest = max(length, longest)
        return longest

nigga = [1, 2, 3, 5, 8, 9, 10, 11]