class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return min(nums)

        l = 0
        r = len(nums)-1

        while l < r:
            mid = l + ((r-l)//2)

            # compare l, mid, r?
            # normally, l < mid < r
            if nums[l] > nums[mid]:
                if nums[mid] < nums[mid-1]:
                    return nums[mid]
                r = mid-1

            elif nums[r] < nums[mid]:
                l = mid + 1
            
            else: 
                # just the leftmost element?
                print('returning here')
                return nums[l]
        
        return nums[l]