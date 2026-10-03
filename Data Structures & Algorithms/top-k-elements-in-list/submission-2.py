class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create a dict
        count = {}
        # Create n buckets, one for each int in nums, to store freq?
        freq = [[] for i in range(len(nums) + 1)]

        print("Length of freq:", len(freq))

        # Go through nums
        for num in nums:
            # Increment the count in num to get a frequency
            count[num] = 1 + count.get(num, 0)

        print("count", count)

        # Transfer the frequency counts to the hashset, use the
        # count as the key
        for num, cnt in count.items():
            freq[cnt].append(num)
            print(cnt, num)
        print("Freq:", freq)
        
        # Create a results array
        res = []
        # Go backwards through the freq bucket array
        for i in range(len(freq) - 1, 0, -1):
            # Get the nums with the highest counts. Ties are 
            # broken arbitrarily (whichever appears first in 
            # the freq array)
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res