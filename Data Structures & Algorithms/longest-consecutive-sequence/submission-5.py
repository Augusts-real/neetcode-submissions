class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        longest = 0
        current = 1
        if not nums:
            return 0

        for i in range(1, len(nums) ):
            if nums[i] - nums[i-1] == 1:
                current += 1
            else:
                longest = max(longest, current)
                current = 1
        longest = max(longest, current)
        return longest  
