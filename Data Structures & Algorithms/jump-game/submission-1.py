class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReach, curr = 0, 0

        while curr < len(nums):
            if maxReach < curr:
                return False
            maxReach = max(maxReach, nums[curr]+curr)
            curr += 1

        return True