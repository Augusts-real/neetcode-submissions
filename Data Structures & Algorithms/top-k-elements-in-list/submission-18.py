class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}       # {number : frequency}
        buckets = []

        for _ in range(len(nums) + 1):
            buckets.append([])

        for i in nums:
            if i in hash:
                hash[i] += 1
            else:
                hash[i] = 1

        for key, v in hash.items():
            buckets[v].append(key)

        answer = []

        for thing in buckets[::-1]:
            if thing:
                # if len(answer) == k:
                #     break
                answer.extend(thing)
                if len(answer) >= k:
                    break
        return answer
            