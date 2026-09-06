class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = {0:1} # index : prefix value
        pre_m = 1

        for i in range(1, len(nums)):
            pre_m *= nums[i-1]
            prefix[i] = pre_m
        # print(prefix)

        suffix = {len(nums)-1 : 1} # index : suffic value
        pre_s = 1

        for n in range(0, len(nums) - 1)[::-1]:
            pre_s *= nums[n + 1]
            suffix[n] = pre_s

        output = []
        for k in range(len(nums)):
            output.append(prefix[k] * suffix[k])

        return output