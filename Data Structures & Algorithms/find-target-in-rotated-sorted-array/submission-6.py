class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1

        while l <= r:
            # mid = l + ((r-l)//2)
            mid = (l+r) // 2
            if target == nums[mid]:
                return mid

            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
                    
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
            # elif (target > nums[mid] and target > nums[r]) or (target < nums[mid] and target > nums[l]):
            #     #shift left
            #     r = mid-1
            # elif (target < nums[mid] and target < nums[l]) or (target > nums[mid] and target < nums[r]):
            #     #shift right
            #     l = mid+1

        return -1