class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Add all numbers to an unordered set
        
        longestSequenceLength = 0
        numbers = set()

        for i in range(len(nums)):
            numbers.add(nums[i])

        for i in range(len(nums)):
            curr = nums[i]
            currSequenceLength = 1

            if (curr-1) not in numbers:
                while (curr+1) in numbers:
                    currSequenceLength += 1
                    curr += 1

            if currSequenceLength > longestSequenceLength:
                longestSequenceLength = currSequenceLength
        
        return longestSequenceLength