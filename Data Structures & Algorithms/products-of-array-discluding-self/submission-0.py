class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Pre-fix, post-fix

        output = []

        for i, num in enumerate(nums):
            if i > 0:
                output.append(output[i-1]*num)
            else:
                output.append(num)
        
        for i, num in reversed(list(enumerate(nums))):
            if i > 0:
                if i == (len(nums)-1):
                    output[i] = output[i-1] * 1
                else:
                    output[i] = output[i-1] * nums[i+1]
                    nums[i] *= nums[i+1]
            else:
                output[i] = nums[i+1] * 1
            # Go through and manufacture a pre-fix array in output
            # Go backwards through nums
            # 
            # nums: [1, 2, 4, 6]
            # output (pre-fix): [1, 2, 8, 48]
            # nums (post-fix): [1, 24, 12, 6]
            # output: [1*24, 1*12, 2*4, 6*1]
        
        return output