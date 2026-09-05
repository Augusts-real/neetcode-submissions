class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}

        for i in nums:
            hash[i] = hash.get(i, 0) + 1

        buckets = []

        for bucket in range(len(nums) + 1):
            buckets.append([])

        for num, v in hash.items():
            buckets[v].append(num)

        answer = []

        for bucket in reversed(buckets):
            if bucket:
                answer.extend(bucket)
            if len(answer) >= k:
                break

        return answer[:k]