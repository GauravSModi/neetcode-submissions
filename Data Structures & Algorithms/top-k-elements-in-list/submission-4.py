class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        

        heap = [[] for _ in range(len(nums)+1)]

        for i, j in freq.items():
            heap[j].append(i)

        res = []

        for i in range(len(nums), -1, -1):
            if k == 0:
                return res
            if not heap[i]:
                continue
            
            for j in heap[i]:
                res.append(j)
                k -= 1


        return res