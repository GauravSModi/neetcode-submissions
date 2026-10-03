class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, curr_num in enumerate(nums):
            diff = target - curr_num

            diff_index = seen.get(diff)
            if diff_index is not None:
                return [diff_index, i]
            else:
                seen[curr_num] = i