class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create a dict
        count = {}
        # Create n buckets, one for each int in nums, to store freq?
        freq = [[] for i in range(len(nums) + 1)]

        # Go through nums
        for num in nums:
            # Increment the count in num to get a frequency
            count[num] = 1 + count.get(num, 0)

        # Transfer the frequency counts to the hashset
        for num, cnt in count.items():
            freq[cnt].append(num)
            print(cnt, num)
        
        # Create a results array
        res = []
        # Go backwards through the freq bucket array
        for i in range(len(freq) - 1, 0, -1):

            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res