class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for index, i in enumerate(nums):
            dif = target - i # [1, 2, 3, 6] Target -> 5
            if dif in hash:  # {i : index}
                return [hash[dif], index]    # {1 :  0}
            else:
                hash[i] = index
