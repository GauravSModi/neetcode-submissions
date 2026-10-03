class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReach, curr = 0, 0

        while curr < len(nums):
            if maxReach < curr:
                return False
            maxReach = max(maxReach, nums[curr]+curr)
            # print("maxReach: ", maxReach)
            # print("curr: ", curr)
            curr += 1

        return maxReach >= len(nums)-1