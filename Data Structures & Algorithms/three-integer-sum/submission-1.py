class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for left, x in enumerate(nums):

            # if all integers are positive, impossible to sum to 0
            if x > 0:
                break

            # if the leftmost value is the same as the value before it
            # it's already been considered (avoid duplicates)
            if left > 0 and x == nums[left-1]:
                continue

            mid, right = left+1, len(nums)-1

            while mid < right:
                summ = x + nums[mid] + nums[right]

                if summ < 0:
                    mid+=1
                elif summ > 0:
                    right-=1
                else:
                    res.append([x, nums[mid], nums[right]])
                    mid+=1
                    right-=1
                    while nums[mid] == nums[mid-1] and mid < right:
                        mid+=1
                
        return res