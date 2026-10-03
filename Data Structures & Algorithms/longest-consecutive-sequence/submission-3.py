class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs = set()

        for num in nums:
            hs.add(num)

        longest = 0

        for num in nums:
            curr = 1
            if num-1 not in hs:
                temp = num + 1
                while temp in hs:
                    temp += 1
                    curr += 1
                longest = max(longest, curr)

        return longest