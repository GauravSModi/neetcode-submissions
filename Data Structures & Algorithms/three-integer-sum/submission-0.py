class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, x in enumerate(nums):
            if i > 0 and x == nums[i-1]:
                continue

            left, right = i+1, len(nums)-1

            while left < right:
                summ = x + nums[left] + nums[right]

                if summ < 0:
                    left+=1
                elif summ > 0:
                    right-=1
                else:
                    res.append([x, nums[left], nums[right]])
                    left+=1
                    right-=1
                    while nums[left] == nums[left-1] and left < right:
                        left+=1
                
        return res