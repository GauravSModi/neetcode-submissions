class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        buckets = [[] for i in range(len(nums) + 1)]
        for num, frequency in freq.items():
            buckets[frequency].append(num)

        results = []
        for i in range(len(buckets)-1, 0 ,-1):
            for num in buckets[i]:
                results.append(num)
                if len(results) == k:
                    return results
            