class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        

        buckets = [[] for _ in range(len(nums)+1)]

        for i, j in freq.items():
            buckets[j].append(i)

        res = []

        for i in range(len(nums), -1, -1):
            if k == 0:
                return res
            if not buckets[i]:
                continue
            
            for j in buckets[i]:
                res.append(j)
                k -= 1


        return res